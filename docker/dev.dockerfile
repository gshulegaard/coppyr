FROM ubuntu:22.04

RUN apt update && apt install -y python3-pip python3-setuptools python3-dev

# Install requirements for tests
COPY requirements-config.txt /opt/coppyr/requirements-config.txt
COPY requirements-daemon.txt /opt/coppyr/requirements-daemon.txt
COPY requirements-dev.txt /opt/coppyr/requirements-dev.txt
COPY requirements-pkg.txt /opt/coppyr/requirements-pkg.txt
RUN python3 -m pip install \
  -r /opt/coppyr/requirements-config.txt \
  -r /opt/coppyr/requirements-daemon.txt \
  -r /opt/coppyr/requirements-dev.txt \
  -r /opt/coppyr/requirements-pkg.txt

ENV PYTHONPATH /opt/coppyr

# This is mounted in the docker-compose file.
WORKDIR /opt/coppyr
ENTRYPOINT bash