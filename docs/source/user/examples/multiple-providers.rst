Using Multiple Providers
************************

This example shows how to use different LLM providers with OJU.

.. code-block:: python

   from oju.agent import Agent

   # Example with OpenAI
   response_openai = Agent(
       agent_name="general_assistant",
       model="gpt-4",
       provider="openai",
       api_key="your-openai-key",
       prompt_input="Tell me about the weather"
   )
   print("OpenAI response:", response_openai)

   # Example with Anthropic
   response_anthropic = Agent(
       agent_name="general_assistant",
       model="claude-3-opus-20240229",
       provider="claude",
       api_key="your-anthropic-key",
       prompt_input="Tell me about the weather"
   )
   print("\nAnthropic response:", response_anthropic)

   # Example with Google Gemini
   response_gemini = Agent(
       agent_name="general_assistant",
       model="gemini-pro",
       provider="gemini",
       api_key="your-google-key",
       prompt_input="Tell me about the weather"
   )
   print("\nGoogle Gemini response:", response_gemini)
