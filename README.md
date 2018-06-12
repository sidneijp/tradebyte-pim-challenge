# Simples PIM
___

A simple application for PIM (Product Information Management).

## Installation

### Dependecies

- Python 3.6
- Django 2.0
- pipenv 11.10.0

The project uses `pipenv` instead of `pip` to manage python - so there is no `requirements.txt`. To install it, run as root:

```# pip install -U pipenv```

* Whether you want pipenv to install - in case it's unavailable - and use the right version of Python, please install and configure [pyenv](https://github.com/pyenv/pyenv-installer)

Now to install python packages dependencies:

```$ make install```

To run the application - it will be available at [http://localhost:8000/](http://localhost:8000/), the admin at `/admin/` and the API at `/api/`.

```$ make run```

A initial superuser was created when `make install` ran:

```
username:admin

password:pim123mip
```

To activate the virtualenv if it feels necessary, use:

```$ pipenv shell```

**All `make` commands uses virtualenv interpreter without activating it.** 

### Development

Install the `dev-packages` to be able to run tests, generate coverage report, run linter, etc. 

```$ make dev-install```

To run automated tests:

```$ make test```

or run in "watcher mode":

```$ make testd```

to generate tests coverage:

```$ make coverage```

then to see the report result:

```$ make report```

or for "HTML fashion" report:

```$ make html```

*The HTML report will be available at `./htmlcov/index.html` - open it with a web browser.