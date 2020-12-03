<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-postgres-createdb.svg?maxAge=3600)](https://pypi.org/project/django-postgres-createdb/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-postgres-createdb.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-postgres-createdb.py/actions)

### Installation
```bash
$ [sudo] pip install django-postgres-createdb
```

#### Examples
example 1 - management command:

`settings.py`

```python
INSTALLED_APPS+=['django_postgres_createdb']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

```bash
$ python manage.py createdb
$ python manage.py createdb "default"
```

example 2 - python module cli:

`settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

```bash
$ export DJANGO_SETTINGS_MODULE=settings
$ python -m django_postgres_createdb
$ python -m django_postgres_createdb "default"
```

#### Related
+   [django-postgres-createdb](https://pypi.org/project/django-postgres-createdb/)
+   [django-postgres-dropdb](https://pypi.org/project/django-postgres-dropdb/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
