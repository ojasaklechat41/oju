Basic Usage Example
*******************

This example shows how to use OJU for a simple chat interaction.

.. code-block:: python

   from oju.agent import Agent

   # Initialize the agent
   response = Agent(
       agent_name="chat_assistant",
       model="gpt-4",
       provider="openai",
       api_key="your-api-key-here",
       prompt_input="Hello, how can you help me today?"
   )
   
   print(response)

This will send the prompt to the specified model and print the response.
