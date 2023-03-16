# Cancer Data API Code

This project contains all of the source code for the Cancer Data API web service.

## Initial project setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks (if needed)
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Running tests

Run the tests for this project with

```bash
pipenv run pytest
```

## Updating dependencies

Dependencies need to be installed in the virtual environment for the project to run successfull as described above. Dependencies should be added to the appropriate section in Pipfile and

```bash
pipenv install --dev
```

should be re-run as needed.

## Development in Eclipse

This project works fine as a PyDev project. Please note that Eclipse is not setup to use Pytest by default, so test run configurations must be edited manually to run it. Likewise, Eclipse does not use the virtual environment, so dependencies must be installed for the Python install used by Eclipse. This is likely the system default, but it is also possible to configure a custom install or pyenv.

## Credits
The initial structure of this package was generated with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
