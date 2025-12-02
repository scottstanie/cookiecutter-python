## Install


`{{cookiecutter.project_name}}` is available on conda-forge and can be installed with pixi:

```bash
pixi add {{cookiecutter.project_name}}
```


## Usage

Example usage:


## Setup for Developers

To contribute to the development of `{{cookiecutter.project_name}}`, you can fork the repository and install the package in development mode.
We encourage new features to be developed on a new branch of your fork, and then submitted as a pull request to the main repository.

To install locally,

1. Download source code:
```bash
git clone {{cookiecutter.url}}
```
2. Install dependencies and the package:
```bash
pixi install
```

The extra packages required for testing and building the documentation can be installed:
```bash
pixi install --environment test
# or: pixi shell --environment test
pixi install --environment docs
```

We use [`pre-commit`](https://pre-commit.com/) to automatically run linting and formatting:
```bash
# Get pre-commit hooks so that linting/formatting is done automatically
pixi shell --environment test
pre-commit install
```
This will set up the linters and formatters to run on any staged files before you commit them.

After making functional changes, you can rerun the existing tests and any new ones you have added using:
```bash
pixi run -e test pytest
# or, if in the test shell environment: pytest
```

### Creating Documentation

We use [MkDocs](https://www.mkdocs.org/) to generate the documentation.
The reference documentation is generated from the code docstrings using [mkdocstrings](mkdocstrings.github.io/).

When adding new documentation, you can build and serve the documentation locally using:

```
pixi run mkdocs serve
```
then open http://localhost:8000 in your browser.
Creating new files or updating existing files will automatically trigger a rebuild of the documentation while `mkdocs serve` is running.
