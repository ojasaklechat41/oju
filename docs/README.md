# OJU Documentation

This directory contains the source files for the OJU documentation.

## Building the Documentation

1. Install the required dependencies:
   ```bash
   pip install -r requirements-docs.txt
   ```

2. Build the documentation:
   ```bash
   make clean
   make html
   ```

3. View the documentation by opening `build/html/index.html` in your browser.

## Documentation Structure

- `source/user/` - User documentation and guides
- `source/development/` - Developer documentation and contribution guides
- `source/examples/` - Example usage and tutorials

## Contributing

Please see the [Contributing Guide](../CONTRIBUTING.md) for information on how to contribute to the documentation.
