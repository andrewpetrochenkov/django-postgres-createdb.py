#!/usr/bin/env python
"""create postgres database"""
# -*- coding: utf-8 -*-
import click
import django
from django.conf import settings
import subprocess
import os
import sys

MODULE_NAME = "django_postgres_createdb"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [alias]' % MODULE_NAME


@click.command()
@click.argument('alias',required=False)
def _cli(alias=None):
    if not alias:
        alias = "default"
    DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')
    if not DJANGO_SETTINGS_MODULE:
        sys.exit("DJANGO_SETTINGS_MODULE unknown")
    django.setup()
    db_settings = settings.DATABASES[alias]
    args = ['createdb']
    if 'USER' in db_settings:
        args+=["-O",db_settings['USER']]
    if 'HOST' in db_settings:
        args+=["-h",db_settings['HOST']]
    if 'PORT' in db_settings:
        args+=["-p",str(db_settings['PORT'])]
    args.append(db_settings['NAME'])
    subprocess.check_call(args)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
