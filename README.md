GP Sign Up
===========

###INFO
version: full
branch: REST_experiment

===========

###SETTINGS
to run with various settings:
'''
python manage.py runserver --settings=<project_name>.settings.<mode>
'''
(e.g.) python manage.py runserver --settings=twoscoops.settings.local

===========

###MIGRATION
to create and migrate db using south:
'''
python manage.py schemamigration <app_name> --initial --settings=<project_name>.settings.<mode>
python manage.py migrate <app_name> --fake --settings=<project_name>.settings.<mode>
'''

if you change models, repeat the following:
'''
python manage.py schemamigration <app_name> --auto --settings=<project_name>.settings.<mode>
python manage.py migrate <app_name> --settings=<project_name>.settings.<mode>
'''

souces:
* http://stackoverflow.com/questions/12784835/django-no-such-table
* http://south.readthedocs.org/en/latest/commands.html

===========

###SECRET_KEY
use env variable to manage SECRET_KEY's:
'''
export SECRET_KEY=y34h-r1ght-d0nt-t0uch-my-1c3-cr34m
'''

to access env in Python (e.g. settings/production.py)
'''
import os
SOME_SECRET_KEY = os.environ["SOME_SECRET_KEY"]
'''

refer to "2 Scoops of Django" for exception handling

set environment varible in production:
'''
heroku config:add SOME_SECRET_KEY=1c3-cr3am-15-yummy
'''

===========

###REQUIREMENTS
to setup using a requirement file, in repo directory:
'''
pip install -r requirements/<req_file>.txt
'''
(e.g.) pip install -r requirements/local.txt

to generate current requirements:
'''
pip freeze --local
'''