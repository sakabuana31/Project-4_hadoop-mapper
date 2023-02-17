#!/bin/bash

# create new network
docker network create hadoop_network

# build docker image dengan nama image hadoop-base:3.3.1, bakal cari file bernama Dockerfile
docker build -t hadoop-base:3.3.1 .

# untuk running image menjadi container, -d untuk berjalan secara background, bakal mencari file bernama docker-compose-hadoop.yml
docker-compose -f docker-compose-hadoop.yml up -d
