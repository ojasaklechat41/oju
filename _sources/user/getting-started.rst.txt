Getting Started
***************

This guide will help you quickly get started with OJU and make your first API call.

Prerequisites
*************
- Python 3.8 or higher
- An API key from one of the supported providers (OpenAI, Anthropic, or Google Gemini)

Installation
************

.. include:: installation.rst
   :start-after: Installation
   :end-before: Basic Usage

Your First API Call
*******************

Here's a simple example to get you started with OJU:

.. code-block:: python

   from oju.agent import Agent

   response = Agent(
       agent_name="example_agent",
       model="gpt-4",
       provider="openai",
       api_key="your-api-key-here",
       prompt_input="Hello, how are you?"
   )
   print(response)

Next Steps
**********
- Learn about :doc:`working with prompts <prompts>`
- Explore the :doc:`API Reference <../development/api>`
- Check out the :doc:`examples <examples/index>`
