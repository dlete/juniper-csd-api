# Installation instructions

Two flavours: with Docker and with Python Virtual Environment

## Docker

<https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run>
<https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/>
<https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file>
<https://github.com/dockerfile/ubuntu/blob/master/Dockerfile>

Create the image

```bash
docker build -t myimage .
docker build -t jnpr_csd_api/ubuntu:16.04 .
docker build -f Dockerfile.dev -t jnpr_csd_api/ubuntu:16.04 .
```

repository>:<tag

Run the container

```bash
# docker run -ti --rm -v ${PWD}:/app myimage
# docker run -ti --rm -v ${PWD}:/app 
docker run -ti -v ${PWD}:/app --rm --name jnpr_csd_api jnpr_csd_api/ubuntu:16.04
```

```bash
cat /etc/issue
```

## Virtualenv

### Create a virtual environment for this project

* Install `apt-get install python3-venv`, this is necessary to create virtual environments with Python3.

```bash
sudo apt-get install python3-venv
```

* Create a virtual environment. Then activate the virtual environment.

```bash
python3 -m venv </path/to/new/virtual/environment>
source </path/to/new/virtual/environment>/bin/activate
```

I find it convenient in the the root of the project

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Clone the code

```bash
git clone <url>
```

### Install Python packages

Upgrade `pip` in the virtual environment

```bash
pip install --upgrade pip
```

Install the Python packages

```bash
pip install -r requirements.txt
```
