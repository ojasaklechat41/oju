Using Custom Prompts
********************

This example demonstrates how to use custom system prompts with OJU.

.. code-block:: python

   from oju.agent import Agent

   # Define a custom system prompt
   custom_prompt = """
   You are a helpful coding assistant. Your responses should be:
   - Concise and to the point
   - Include code examples when relevant
   - Use markdown formatting for better readability
   """

   # Initialize the agent with custom prompt
   response = Agent(
       agent_name="code_assistant",
       model="gpt-4",
       provider="openai",
       api_key="your-api-key-here",
       prompt_input="How do I reverse a list in Python?",
       custom_system_prompt=custom_prompt
   )
   
   print(response)
