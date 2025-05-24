import os
from typing import Optional
from . import providers

def Agent(
    agent_name: str,
    model: str,
    provider: str,
    api_key: str,
    prompt_input: str,
    custom_system_prompt: Optional[str] = None
) -> str:
    """
    Executes an agent using the specified model provider and prompt.

    Args:
        agent_name: Name of the agent (used to locate prompt file).
        model: Name of the model to use (e.g., 'gpt-4', 'claude-3-opus').
        provider: One of 'openai', 'claude', or 'gemini'.
        api_key: API key for the respective provider.
        prompt_input: User input to be processed by the agent.
        custom_system_prompt: Optional custom system prompt that overrides the file-based one.

    Returns:
        str: The generated response from the model.

    Raises:
        FileNotFoundError: If the prompt file is not found.
        ValueError: If the prompt file is empty or provider is unsupported.
        Exception: For errors during API calls to the model providers.
    """
    # Use custom prompt if provided, otherwise load from file
    if custom_system_prompt is not None:
        system_prompt = custom_system_prompt.strip()
    else:
        prompt_path = os.path.join(
            os.path.dirname(__file__), "prompts", agent_name, "prompt.txt"
        )
        try:
            with open(prompt_path, "r", encoding='utf-8') as f:
                system_prompt = f.read().strip()
            if not system_prompt:
                raise ValueError(f"Prompt file {prompt_path} is empty")
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Prompt file not found: {prompt_path}. "
                "Please ensure the agent_name corresponds to an existing prompt directory."
            ) from e
    
    if not api_key:
        raise ValueError(f"API key for {provider} is required")
    
    if not prompt_input or not prompt_input.strip():
        raise ValueError("Prompt input cannot be empty")
    
    # Map of supported providers to their respective functions
    provider_functions = {
        "openai": providers.call_openai,
        "claude": providers.call_claude,
        "gemini": providers.call_gemini,
    }
    
    if provider not in provider_functions:
        raise ValueError(
            f"Unsupported provider: {provider}. "
            f"Supported providers are: {', '.join(provider_functions.keys())}"
        )
    
    try:
        # Call the appropriate provider function
        return provider_functions[provider](
            model=model,
            system_prompt=system_prompt,
            prompt=prompt_input,
            api_key=api_key
        )
    except Exception as e:
        raise Exception(
            f"Error getting completion from {provider} ({model}): {str(e)}"
        ) from e