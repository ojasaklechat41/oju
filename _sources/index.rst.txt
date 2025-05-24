.. OJU documentation master file

Welcome to OJU's Documentation!
*******************************

OJU is a lightweight Python library that provides a unified interface for interacting with multiple
large language model (LLM) providers, including OpenAI, Anthropic, and Google Gemini. It simplifies
the process of creating and managing AI agents with structured prompts.

Choose your documentation:

.. grid:: 1 2 2 2
   :gutter: 5

   .. grid-item::
      :class: sd-fs-5 text-center
      
      **User Guide**
      
      .. button-ref:: user/index
         :ref-type: doc
         :class: sd-stretched-link
      
      Learn how to use OJU in your projects.

   .. grid-item::
      :class: sd-fs-5 text-center
      
      **Developer Docs**
      
      .. button-ref:: development/index
         :ref-type: doc
         :class: sd-stretched-link
      
      Contribute to OJU or understand its internals.

Key Features
************

- **Multi-provider support**: Switch between different LLM providers with a single interface
- **Structured prompts**: Organize your prompts in files for better maintainability
- **Simple API**: Easy-to-use function-based interface for making LLM calls
- **Flexible configuration**: Configure models and providers programmatically or via environment variables

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: User Guide:
   
   user/index

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Development:
   
   development/index

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
