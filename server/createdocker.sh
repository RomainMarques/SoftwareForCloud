#!/bin/bash

docker build -t cloud_backend:0.1 . && \
docker run -it -p 3000:3000 --name cloud_backend cloud_backend:0.1