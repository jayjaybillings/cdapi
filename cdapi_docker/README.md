# Cancer Data API Docker Package

This project contains all the docker configuration info for the Cancer Data API web service.

Starting the CDAPI webservice in Docker container is a two step process. First, the image that will run inside the container needs to be built. Second, the container needs to be started with port forwarding to the host.

## Build the Docker Image

Build the Docker image with the following command from inside the cdapi_docker directory:

```bash
docker build -t cdapi .. -f Dockerfile
```

There are some important notes here. It is important for the scope of the docker build command to be set to the parent directory that holds both `cdapi` and `cdapi_docker` so that the source code can be copied correctly into the image. Also, the `build` command behaves differently if the Dockerfile is omitted, so it should be explicitly specified as well.

## Run the Docker Container

The following command will run the CDAPI Docker container that was built in the previous step and make the API available on port 8000 of the host.

```bash
docker run -p 8000:80 cdapi
```

If this command runs successfully, navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the API docs.