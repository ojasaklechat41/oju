from setuptools import setup, find_packages

# Read the README for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='oju',
    version='0.1.0',
    author='Ojas Aklecha',
    author_email='ojasaklechayt@gmail.com',
    description='A multi-agent framework supporting multiple LLM providers with structured prompts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ojasaklechat41/oju',
    packages=find_packages(),
    package_data={
        'oju': ['prompts/**/*.txt'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    install_requires=[
        'openai>=1.0.0',
        'anthropic>=0.3.0',
        'google-generativeai>=0.3.0',
        'python-dotenv>=0.19.0',
    ],
    python_requires='>=3.8',
    keywords='llm ai agent framework openai anthropic gemini',
    project_urls={
        'Bug Reports': 'https://github.com/ojasaklechat41/oju/issues',
        'Source': 'https://github.com/ojasaklechat41/oju',
    },
)
