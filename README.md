# simao-ferreira static website

Static site created using [pelican](https://docs.getpelican.com/en/4.7.1/index.html)

Pelican is a python static site generator the uses jinja templating for displaying content created in markdown.

Site is deployed with GitHub actions.

- [how-to](#how-to)
    - [setup](#setup)
    - [build](#build-and-run)
    - [tests](#tests)
    - [configuration](#configuration)
    - [problems](#problems)
- [technologies](#technologies)
- [references](#references)

## how to

### setup

Create a new environment

```shell
$ python3 -m venv static-venv
```

Activate environment

```shell
$ source static-venv/bin/activate
```

Install pip-tools

```shell
$ pip install pip-tools
```

Update requirements.txt

```shell
$ pip-compile --upgrade requirements.in
```

Install dependencies

```shell
$ pip install -r requirements.txt
```

Deactivate

```shell
$ deactivate
```

### build and run

Build server

```shell
$ make devserver
```

Or - without make

```shell
$ cd output
$ pyhton -m http.server
``` 

### tests

```shell
# Run all tests
$ pytest

# Run class test
$ pytest tests/ <test_file_name >.py

```

### configuration

### problems

## technologies

|    python packages     |
| :-------------: |
|pelican|
|markdown|
|tzlocal|

## references

1. https://www.fullstackpython.com/pelican.html
2. https://cloudbytes.dev/snippets/automate-deployment-of-pelican-website-to-github-pages
3. http://www.pelicanthemes.com/
