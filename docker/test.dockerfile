FROM ubuntu:22.04

RUN apt update && apt install -y python3-pip python3-setuptools python3-dev

# Install requirements for tests
COPY requirements.txt /opt/coppyr/requirements.txt
COPY requirements-test.txt /opt/coppyr/requirements-test.txt
RUN python3 -m pip install -r /opt/coppyr/requirements-test.txt

ENV PYTHONPATH /opt/coppyr

# This is mounted in the docker-compose file.
WORKDIR /opt/coppyr
ENTRYPOINT bash