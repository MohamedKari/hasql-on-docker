FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"] 

##### PYENV & PYTHON #####
# Install pyenv dependencies & pyenv itself
# see: https://github.com/pyenv/pyenv/wiki/common-build-problems
RUN ln -snf /usr/share/zoneinfo/UTC /etc/localtime && echo UTC > /etc/timezone
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git && \
    git clone --single-branch --depth 1  https://github.com/pyenv/pyenv.git /.pyenv

ENV PYENV_ROOT="/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
ENV PATH="$PYENV_ROOT/shims:$PATH"

ARG PYTHON_VERSION=3.8.9

RUN pyenv install ${PYTHON_VERSION} && \
    pyenv global ${PYTHON_VERSION}

ENV PYTHONUNBUFFERED=.

##### APP #####

# Install package dependencies
RUN pip install fastapi==0.68.0 uvicorn==0.14.0

COPY app /app

WORKDIR /app

ENTRYPOINT [ "python", "server.py" ]


# USAGE
# -----
# docker build --tag dbservice .
# docker run -e LICENSE_KEY=SCOTLAND -p 9000:8000 dbservice
# curl http://localhost:9000/user/3