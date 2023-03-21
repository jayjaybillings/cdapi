FROM python:3.10-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Pipenv needs a good working directory and having a normal user is a good idea
# as well, so create an account and home directory.
RUN useradd --create-home cdapi_user
WORKDIR /home/cdapi_user
# Add code and fix permissions
ADD cdapi cdapi
RUN chown -R cdapi_user:cdapi_user /home/cdapi_user
# Change to the new user
USER cdapi_user

# Install dependencies
WORKDIR /home/cdapi_user/cdapi
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
# Add the cdapi directory
#COPY cdapi/Pipfile .
#RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# Run the executable
#ENTRYPOINT ["ls","-lah","/home/cdapi_user/cdapi"]
ENTRYPOINT ["pipenv","run"]
CMD ["uvicorn", "cdapi.CCLE_web_service:app", "--host","0.0.0.0","--port","80"]
