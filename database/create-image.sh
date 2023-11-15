#!/bin/bash

docker build --build-arg MYSQL_ROOT_PASSWORD=root --build-arg MYSQL_DATABASE=projet_cloud -t sql_cloud_projet:0.1 . && \
docker run -it -d -p 8080:3306 --name sql_cloud_projet sql_cloud_projet:0.1