# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim as base

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
#ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/server
#COPY Flat_page.html /usr/src/server
COPY server.py /usr/src/server

# Copy the source code into the container.
COPY . /usr/src/server

# Expose the port that the application listens on.
EXPOSE 8080

# Run the application.
CMD python server.py
