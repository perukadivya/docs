# Local Setup

## Prerequisites

- Python 3.9+
- pip

## Installation

```bash
# Clone the repository
git clone https://github.com/your-org/data-engineering-docs.git
cd data-engineering-docs

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Build Locally

```bash
# Build the documentation
jupyter-book build .

# The output will be in _build/html/
# Open _build/html/index.html in your browser
```

## Live Preview

For live preview during development:

```bash
pip install sphinx-autobuild
sphinx-autobuild . _build/html
```

```{tip}
The live preview will automatically refresh when you save changes to any markdown file.
```
