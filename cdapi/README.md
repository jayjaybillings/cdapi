# Cancer Data API Code

This project contains all of the source code for the Cancer Data API web service.

## Initial project setup

This project uses Python Virtual Environments to install all packages and configuration settings on top of the/an existing python installation. The virtual environment is configured and accessed with `pipenv`.

```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks (if needed)
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Running tests

Run the tests for this project from the root directory with

```bash
pipenv run pytest
```

Be sure to use the root directory to
1. Catch the right paths for the test date
2. Allow the tests to import cdapi correctly

## Running the server

This project uses FastAPI and Uvicorn to publish the data api. Start the server as follows:

```bash
pipenv run uvicorn cdapi.CCLE_web_service:app --reload
```

Follow the instructions on screen to find the service loaded at
[http://127.0.0.1:8000](http://127.0.0.1:8000). Follow the links on
that page to interact with the API.

## Updating dependencies

Dependencies need to be installed in the virtual environment for the project to run successfully as described above. Dependencies are installed with

```bash
pipenv install --dev
```

If the pipfile changes, either because a dependency was added or removed, run

```bash
pipenv update
```
In some cases, it may be necessary to run the install command again if the pipfile changes, but generally updates are sufficient.

The list of installed packages can be manually verified with

```bash
pipenv graph
```

## Development in Eclipse

This project works fine as a PyDev project. Please note that Eclipse is not setup to use Pytest by default, so test run configurations must be edited manually to run it. Likewise, Eclipse does not use the virtual environment, so dependencies must be installed for the Python install used by Eclipse. This is likely the system default, but it is also possible to configure a custom install or pyenv.

## Credits
The initial structure of this package was generated with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
