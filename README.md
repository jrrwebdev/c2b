# JRRWEBDEV
- The name originated from the first letter of the name of each member of the faculty working group(very creative!).
- We were originally composed of three members. Juliana, Reinaldo e Ricardo.

# Project Description
This project  web plataform consumer to Business.

# Dropbox Documentation
https://www.dropbox.com/sh/d3zzqrjf62shs99/AADNQYOqfs6cqtGp6mKLMkj_a?dl=0



Getting Started
---------------

# Initial Setup
* Make a new virtualenv: ``virtualenv .venv``
* Activate the virtualenv: ``source .venv/bin/activate``
* Install Django: ``pip install -r requirements.txt``
* Run the server: ``python manage.py runserver``
* Admin Site at ``http://127.0.0.1:8000/admin``



### Deploy ###
1. should be Completed


# Unit Tests 
* should be completed

# Docker
* shoud be completed
```sh

   Build docker container
   docker build -t myapplication .

   Running container
   docker run -p 8000:8000 -d myapplication

  # Dockerfile for Django Rest API development environment
  # Based on Ubuntu Image

  FROM ubuntu
   MAINTAINER NeuralFoundry <neuralfoundry.com>

   RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >> /etc/apt/sources.list
   RUN apt-get update

   ## Python Family
   RUN apt-get install -qy python python-dev python-distribute python-pip ipython


   # Replace 1000 with your user / group id
   RUN export uid=1000 gid=1000 && \
       mkdir -p /home/developer && \
       echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
       echo "developer:x:${uid}:" >> /etc/group && \
       echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
       chmod 0440 /etc/sudoers.d/developer && \
       chown ${uid}:${gid} -R /home/developer

   USER developer
   ENV HOME /home/developer
```

#Alterações feitas
Foi inserida um style.css, não sabia onde inserir aqueles dados
Alterei um pouco as cores também, para combinar mais