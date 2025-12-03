FROM mcr.microsoft.com/devcontainers/python:3.14

#
# RUN nvm install stable
# ENV NVM_DIR="/usr/local/share/nvm"

RUN curl -sL https://aka.ms/InstallAzureCLIDeb
COPY requirements.txt .
RUN pip install --upgrade pip; pip install -r requirements.txt


# RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install stable"