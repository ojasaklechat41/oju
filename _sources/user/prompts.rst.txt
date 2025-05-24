Working with Prompts
********************

OJU is designed to work with structured prompts stored in files, allowing for better organization
and maintainability of your prompts. This document covers how to use the built-in agents and how to
add your own custom agents.

Available Agents
****************

OJU comes with specialized agents that can be used by specifying their exact agent name. The current available agents are:

- ``backend_coding_agent`` - For backend development tasks and API design
- ``frontend_coding_agent`` - For frontend development and UI/UX tasks

.. note::
   New agents will be added continuously to expand OJU's capabilities. Always check the latest documentation or the ``oju/prompts`` directory for the most up-to-date list of available agents.

Using Built-in Agents
*********************

To use a built-in agent, simply specify the agent name when initializing the Agent class:

.. code-block:: python

    from oju.agent import Agent

    # Using the backend coding agent
    backend_response = Agent(
        agent_name="backend_coding_agent",
        model="gpt-4",
        provider="openai",
        api_key="your-api-key-here",
        prompt_input="How do I implement a REST API in FastAPI?"
    )

Adding Custom Agents (For Developers)
*************************************

The OJU team continuously adds new agents to the package. You can check the latest available agents by listing the contents of the ``oju/prompts`` directory.

To add your own custom agent to the OJU package, follow these steps:

1. Create a new directory in ``oju/prompts/`` with your agent's name (e.g., ``my_custom_agent/``)
2. Inside this directory, create a ``prompt.txt`` file containing your agent's system prompt
3. The prompt file should define the agent's behavior, capabilities, and limitations

Example structure for a new agent::

    oju/
    └── prompts/
        └── my_custom_agent/
            └── prompt.txt

.. note::
   After adding a new agent directory with its ``prompt.txt``, the agent will be automatically detected and available for use in your code. The agent name will be the same as the directory name you created.

Best Practices for Agent Prompts
********************************

1. **Clear Instructions**: Clearly define the agent's purpose and behavior
2. **Input/Output Formatting**: Specify expected input formats and how outputs should be structured
3. **Safety Guidelines**: Include safety instructions and content moderation rules
4. **Examples**: Provide examples of good inputs and expected outputs
5. **Tone and Style**: Define the communication style (formal, casual, technical, etc.)

Overriding Prompts
******************

You can override the default prompt by using the ``custom_system_prompt`` parameter:

.. code-block:: python

    from oju.agent import Agent

    custom_prompt = """
    You are a technical expert in Python programming.
    Provide detailed code examples and explanations.
    """

    response = Agent(
        agent_name="backend_coding_agent",  # Base agent
        model="gpt-4",
        provider="openai",
        api_key="your-api-key-here",
        prompt_input="How do I use list comprehensions in Python?",
        custom_system_prompt=custom_prompt  # Overrides the default prompt
    )

Best Practices
**************

1. **Organize by Agent**: Keep prompts for different agents in separate directories
2. **Version Control**: Track changes to your prompts in version control
3. **Environment Variables**: Use environment variables for API keys and sensitive information
4. **Testing**: Test your prompts thoroughly before deploying to production
5. **Documentation**: Document the expected inputs and outputs for each prompt
