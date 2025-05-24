# OJU - Multi-Agent Framework for LLMs

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/ojasaklechat41/oju/actions/workflows/tests.yml/badge.svg)](https://github.com/ojasaklechat41/oju/actions)
[![codecov](https://codecov.io/gh/ojasaklechayt/oju/graph/badge.svg?token=YOUR_TOKEN_HERE)](https://codecov.io/gh/ojasaklechayt/oju)

OJU is a lightweight, extensible framework for building and managing AI agents powered by various large language models (LLMs) including OpenAI, Anthropic, and Google's Gemini.

## ✨ Features

- **Multi-Provider Support**: Seamlessly switch between different LLM providers (OpenAI, Anthropic, Gemini)
- **Structured Prompts**: Organize and manage your prompts in a clean, file-based system
- **Simple API**: Easy-to-use interface for interacting with different LLM providers
- **Extensible**: Add support for new LLM providers with minimal code
- **Type Hints**: Full type annotations for better development experience
- **Comprehensive Testing**: Thorough test coverage for reliable operation
- **Documentation**: Extensive documentation with examples
- **Custom System Prompts**: Override default prompts on the fly
- **Error Handling**: Robust error handling with meaningful messages

## Installation

Install OJU using pip:

```bash
pip install oju
```

For development:

```bash
git clone https://github.com/ojasaklechat41/oju.git
cd oju
pip install -e ".[dev]"
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- API keys for your preferred LLM providers

### Installation

Install OJU using pip:

```bash
pip install oju
```

### Setting Up API Keys

Set your API keys as environment variables or in a `.env` file:

```bash
# .env file
OPENAI_API_KEY='your-openai-key'
ANTHROPIC_API_KEY='your-anthropic-key'
GOOGLE_API_KEY='your-google-key'
```

### Basic Usage

```python
from oju.agent import Agent

# Initialize the agent with OpenAI
response = Agent(
    agent_name="agent_name",
    model="gpt-4-turbo",
    provider="openai",
    api_key="your-api-key",  # or use environment variables
    prompt_input="What's the weather like today?",
    custom_system_prompt="You are a helpful weather assistant."  # Optional override
)

print(response)
```

### Example with Environment Variables

```python
import os
from oju.agent import Agent

# Using environment variables
response = Agent(
    agent_name="agent_name",
    model="claude-3-opus-20240229",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    provider="claude",
    prompt_input="Tell me a joke about programming"
)
print(response)
```

### Expected Output

```
Why do programmers prefer dark mode?
Because light attracts bugs! 🐛
```

## Available Models

| Provider | Supported Models |
|----------|------------------|
| OpenAI  | gpt-4, gpt-3.5-turbo, etc. |
| Anthropic | claude-3-opus-20240229, claude-3-sonnet-20240229, etc. |
| Google Gemini | gemini-pro, gemini-1.5-pro |

## 🛠 Advanced Usage

### Environment Configuration

For better security and flexibility, manage your configuration using environment variables or a `.env` file:

```python
# .env file
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
```

### Error Handling

Handle different types of errors gracefully:

```python
from oju.agent import Agent

try:
    response = Agent(
        agent_name="expert",
        model="gpt-4",
        provider="openai",
        api_key="invalid_key",
        prompt_input="Your question here"
    )
    print(response)
except ValueError as e:
    print(f"Validation error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Working with Different Providers

Switch between different LLM providers with ease:

```python
# Using Anthropic Claude
claude_response = Agent(
    agent_name="expert",
    model="claude-3-opus-20240229",
    provider="claude",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    prompt_input="Explain quantum computing in simple terms"
)

# Using Google Gemini
gemini_response = Agent(
    agent_name="expert",
    model="gemini-pro",
    provider="gemini",
    api_key=os.getenv("GOOGLE_API_KEY"),
    prompt_input="What are the latest trends in AI?"
)
```

### Performance Optimization

For better performance with large prompts or multiple requests:

```python
from concurrent.futures import ThreadPoolExecutor
from oju.agent import Agent

def process_query(query):
    return Agent(
        agent_name="expert",
        model="gpt-4",
        provider="openai",
        api_key=os.getenv("OPENAI_API_KEY"),
        prompt_input=query
    )

queries = ["Query 1", "Query 2", "Query 3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(process_query, queries))

for result in results:
    print(result)
```

## 🛠 Development

We welcome contributions! If you're interested in contributing to OJU, please read our [Contributing Guidelines](CONTRIBUTING.md).

### Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) (recommended) or pip
- Git

### Installation

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/your-username/oju.git
   cd oju
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   # Using pip
   pip install -e ".[dev]"
   
   # Or using Poetry
   poetry install
   ```

### Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=oju --cov-report=term-missing

# Run a specific test file
pytest tests/test_agent.py -v

# Run tests with detailed output
pytest -v
```

### Code Quality

We use several tools to maintain code quality:

```bash
git clone https://github.com/ojasaklechat41/oju.git
cd oju
pip install -e ".[dev]"
```

### Documentation

Build the documentation locally:

```bash
cd docs
make html
open _build/html/index.html  # Open in browser
```

For test coverage:

```bash
pytest --cov=oju
```

### Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -m "Add your feature"`
3. Push to the branch: `git push origin feature/your-feature`
4. Open a Pull Request

### Release Process

1. Update the version in `pyproject.toml`
2. Update `CHANGELOG.md` with the new version
3. Create a new release on GitHub
4. Publish to PyPI:
   ```bash
   rm -rf dist/*
   python -m build
   twine upload dist/*
   ```

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

For detailed information on how to contribute, please see our [Contributing Guide](CONTRIBUTING.md).

### Ways to Contribute

- Report bugs by [opening a new issue](https://github.com/ojasaklechat41/oju/issues/new/choose)
- Suggest new features or enhancements
- Submit pull requests for bug fixes or new features
- Improve documentation
- Add test cases
- Spread the word about OJU

## 📞 Contact

Ojas Aklecha 
- Twitter: [@ojasaklecha](https://twitter.com/ojasaklecha)
- Email: ojasaklechayt@gmail.com
- GitHub: [@ojasaklechayt](https://github.com/ojasaklechat41)

Project Link: [https://github.com/ojasaklechat41/oju](https://github.com/ojasaklechat41/oju)

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for their amazing language models
- [Anthropic](https://www.anthropic.com/) for Claude models
- [Google AI](https://ai.google/) for Gemini models
- All the contributors who helped improve this project

---

<div align="center">
  Made with ❤️ by Ojas Aklecha | 2025
</div>
