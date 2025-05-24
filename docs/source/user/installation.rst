Installation
============

.. code-block:: bash

   # Install from PyPI
   pip install oju

   # Or install from source
   git clone https://github.com/ojasaklechat41/oju.git
   cd oju
   pip install -e .

Dependencies
------------

OJU requires Python 3.8 or higher and the following packages:

- openai>=1.0.0
- anthropic>=0.3.0
- google-generativeai>=0.3.0
- python-dotenv>=0.19.0

Optional development dependencies can be installed with:

.. code-block:: bash

   pip install -e ".[dev]"
