Sample Django App
=================
Django-powered REST API for bookmarking URLs and websites.


Prerequisites
-------------
You need to have Python 3.8+ and Pipenv installed on your local machine.


Run on development machine
--------------------------
1.  Change current working directory into the root directory of this repo.

2.  Create new virtual environment directory for Pipenv:

        mkdir .venv

3.  Install dependencies:

        pipenv install

4.  Run DB migration:

        pipenv run ./manage.py migrate

5.  Run the development server on port 3000:

        pipenv run ./manage.py runserver 3000

6.  Visit `http://localhost:3000` using your browser to open the Browsable API.


LICENSE
-------
MIT
