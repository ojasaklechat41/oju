Contributing
************

We welcome contributions to OJU! Here's how you can help:

Reporting Issues
****************

- Check the `issue tracker <https://github.com/ojasaklechat41/oju/issues>`_ to see if the issue has already been reported
- If not, create a new issue with a clear title and description
- Include steps to reproduce the issue and any relevant error messages
- Specify your Python version and the versions of any relevant packages

Development Setup
*****************

1. **Fork the repository**

   .. code-block:: bash

      git clone https://github.com/ojasaklechat41/oju.git
      cd oju

2. **Set up a virtual environment** (recommended)

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install development dependencies**

   .. code-block:: bash

      pip install -e ".[dev]"

4. **Run tests**

   .. code-block:: bash

      pytest

Code Style
**********

- Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide
- Use type hints for all function parameters and return values
- Keep functions small and focused on a single responsibility
- Write docstrings for all public functions and classes
- Run ``black`` and ``isort`` before committing

Pull Request Process
********************

1. Create a new branch for your feature/fix:

   .. code-block:: bash

      git checkout -b feature/your-feature-name

2. Make your changes and commit them:

   .. code-block:: bash

      git commit -m "Add your commit message here"

3. Push your changes to your fork:

   .. code-block:: bash

      git push origin feature/your-feature-name

4. Open a Pull Request against the ``main`` branch
5. Ensure all tests pass and the code meets the project's coding standards

Adding a New Provider
*********************

1. Add a new function in ``oju/providers.py`` following the existing pattern
2. Update the ``Agent`` function in ``oju/agent.py`` to include the new provider
3. Add tests for the new provider
4. Update the documentation with the new provider details

Testing
*******

- Write tests for any new functionality
- Ensure all tests pass before submitting a PR
- Run ``pytest`` to run the test suite
- For test coverage, run ``pytest --cov=oju``

Documentation
*************

- Update any relevant documentation when adding new features
- Keep docstrings up-to-date
- Add examples for new functionality

Code of Conduct
***************

This project adheres to the `Contributor Covenant <https://www.contributor-covenant.org/version/2/0/code_of_conduct/>`_. By participating, you are expected to uphold this code.
