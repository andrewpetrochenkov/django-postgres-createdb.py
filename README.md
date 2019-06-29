<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-postgres-createdb.svg?longCache=True)](https://pypi.org/project/django-postgres-createdb/)
[![](https://img.shields.io/pypi/v/django-postgres-createdb.svg?maxAge=3600)](https://pypi.org/project/django-postgres-createdb/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/django-postgres-createdb.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/django-postgres-createdb.py/)

#### Installation
```bash
$ [sudo] pip install django-postgres-createdb
```

#### `settings.py`
```python
INSTALLED_APPS = [
    "django_postgres_createdb",
]
```

#### Commands
command|`help`
-|-
`python manage.py createdb` |create postgres database

#### Examples
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
$ python manage.py createdb
$ python manage.py createdb "default"
```

#### Related projects
+   [django-postgres-createdb](https://pypi.org/project/django-postgres-createdb/)
+   [django-postgres-dropdb](https://pypi.org/project/django-postgres-dropdb/)

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>