Usage
*****

Basic Example
*************

.. code-block:: python

   from oju.agent import Agent

   # Initialize and use an agent
   response = Agent(
       agent_name="example_agent",  # Name of the agent (must correspond to a prompt file)
       model="gpt-4",              # Model to use
       provider="openai",           # Provider: 'openai', 'claude', or 'gemini'
       api_key="your-api-key-here", # API key for the provider
       prompt_input="Hello, how are you?"  # User input
   )
   print(response)

Using Different Providers
*************************

OJU supports multiple LLM providers, with plans to continuously add more in the future. Here's how to use the currently supported providers:

.. code-block:: python

   # Using OpenAI
   response = Agent(
       agent_name="example_agent",
       model="gpt-4",
       provider="openai",
       api_key="your-openai-key",
       prompt_input="Your prompt here"
   )
   
   # Using Anthropic Claude
   response = Agent(
       agent_name="example_agent",
       model="claude-3-opus-20240229",
       provider="claude",
       api_key="your-anthropic-key",
       prompt_input="Your prompt here"
   )
   
   # Using Google Gemini
   response = Agent(
       agent_name="example_agent",
       model="gemini-pro",
       provider="gemini",
       api_key="your-google-key",
       prompt_input="Your prompt here"
   )

.. note::
   The OJU team is continuously working to add support for more LLM providers. Check the latest documentation or release notes for updates on newly added providers.

Using Multiple Agents
*********************

You can run multiple agents in parallel for more complex workflows:

.. code-block:: python

   from concurrent.futures import ThreadPoolExecutor
   from oju.agent import Agent

   def run_agent(agent_config):
       return Agent(**agent_config)

   # Define multiple agent configurations
   agent_configs = [
       {
           'agent_name': 'research_agent',
           'model': 'gpt-4',
           'provider': 'openai',
           'prompt_input': 'Research the latest AI trends',
           'temperature': 0.7
       },
       {
           'agent_name': 'summarizer_agent',
           'model': 'claude-3-opus-20240229',
           'provider': 'claude',
           'prompt_input': 'Summarize this research',
           'temperature': 0.3
       },
       {
           'agent_name': 'critic_agent',
           'model': 'gemini-pro',
           'provider': 'gemini',
           'prompt_input': 'Provide constructive criticism',
           'temperature': 0.5
       }
   ]

   # Run agents in parallel
   with ThreadPoolExecutor() as executor:
       results = list(executor.map(run_agent, agent_configs))

   # Process results
   for i, result in enumerate(results):
       print(f"Agent {i+1} output:")
       print(result)
       print("-" * 50)

Environment Variables
*********************

You can set your API keys as environment variables:

.. code-block:: bash

   # For OpenAI
   export OPENAI_API_KEY='your-api-key-here'
   
   # For Anthropic
   export ANTHROPIC_API_KEY='your-api-key-here'
   
   # For Google Gemini
   export GOOGLE_API_KEY='your-api-key-here'

Or use a `.env` file in your project root:

.. code-block:: bash

   OPENAI_API_KEY=your-api-key-here
   ANTHROPIC_API_KEY=your-api-key-here
   GOOGLE_API_KEY=your-api-key-here
