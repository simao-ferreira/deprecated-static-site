FROM python:3
MAINTAINER Simao Ferreira <email@email.com>

ADD requirements.txt ./

# Update OS
RUN apt-get update
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
RUN apt-get -y upgrade

# Install requirements
RUN pip install -r requirements.txt


WORKDIR /site
# Generate the website when running the container:
CMD pelican content/ -o output/ -s publishconf.py