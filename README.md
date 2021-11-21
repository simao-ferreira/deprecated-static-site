# simao-ferreira static website

Static site created using [pelican](https://docs.getpelican.com/en/4.7.1/index.html)

Pelican is a python static site generator the uses jinja templating for displaying content created in markdown.

Site is deployed with GitHub actions.

- [how-to](#how-to)
    - [environment](#environment)
    - [requirements](#requirements)
    - [build](#build)
    - [run](#run)
    - [tests](#tests)
    - [configuration](#configuration)
    - [problems](#problems)
- [technologies](#technologies)

## how to

### environment

```shell
# Create a new environment
$ python3 -m venv /path/to/new/virtual/environment

# Activate environment
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Deactivate
$ deactivate
```

### requirements

```shell
# Install pip-tools
$ pip install pip-tools

# Generate requirements.txt
$ pip-compile requirements.in

# Update requirements.txt
$ pip-compile --upgrade

# Update single package
$ pip-compile --upgrade-package <package-name>

# Update single package to a specific version
# e.g. --upgrade-package requests==2.0.0
$ pip-compile --upgrade-package <package-name>==<version>
```

### build

Build server

```shell
$ make devserver
```

Or - without make

```shell
$ cd output
$ pyhton -m http.server
```

### run

### tests

```shell
# Run all tests
$ pytest

# Run class test
$ pytest tests/<test_file_name>.py
```

### configuration

### problems

## technologies

|    packages     |
| :-------------: |
|pelican|
|markdown|
|tzlocal|
