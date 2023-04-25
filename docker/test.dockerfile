FROM ubuntu:22.04

RUN apt update && apt install -y python3-pip python3-setuptools python3-dev

# This is mounted in the docker-compose file.
WORKDIR /opt/coppyr
ENTRYPOINT bash