# Flask API Template

This project is aimed at creating initial boiler plate for any flask restful api.

- It provides a basic CRUD functionality for `user` and `product` models
- It also has basic authentication and authorization for users


[Flask API Template](#flask-api-template)

- [Project Setup](#project-setup)
  - [Clone The Repo](#clone-the-repo)
- [Run the app locally using docker](#run-the-app-locally-using-docker)
  - [Install Docker](#install-docker)
  - [Install make](#install-make)
  - [Run the app](#run-the-app)
- [Run the app locally without docker``](#run-the-app-locally-without-docker)
  - [Install PostgreSQL](#install-postgresql)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Activate the virtual environment](#activate-the-virtual-environment)
  - [Install the dependencies](#install-the-dependencies)
  - [Create a .env file](#create-a-env-file)
  - [Run Database migrations](#run-database-migrations)
  - [Run Application](#run-application)
  - [Test the API](#test-the-api)
  - [Checkout Application Api docs](#checkout-application-api-docs)

## Project Setup

Follow these steps to have a local running copy of the app.

### Clone The Repo

`git clone https://github.com/Mubangizi/flask-rest-api-template.git`

If `master` is not up to date, `git checkout develop`. However, note that code on develop could be having some minor issues to sort.

## Run the app locally using docker

### Install Docker

Here's a great resource to check out:

[How To Install and Use Docker on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

### Install make

```bash
sudo apt-get install make
```

### Run the app

To start the app, run

```bash
make start
```

Application should be running on port `5000`

## Run the app locally without docker``

### Install PostgreSQL

Here's a great resource to check out:

[How To Install and Use PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Create a development database and call it `mobile_shop_db`.

### Create a Virtual Environment

create virtual enviroment called `venv` in the root of the project.

Run

```bash
virtualenv venv
```

### Activate the virtual environment

Run

```bash
. venv/bin/activate
```

Make sure you have `pip` installed on your machine.

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Create a .env file

Create a `.env` file (which defines the environment variables used) at the root of the app.

Add the following details, customizing as needed.

```bash
export FLASK_APP=server.py
export DATABASE_URI=postgresql:///flask_app_db
export FLASK_APP_SECRET=qY2i691SX2sEuZ7LUjY480RS48mw5qCeUiyV0i0vzmg
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
```

### Run Database migrations

Run migrations for the database. This will create the tables for the models in the database .

```bash
python manage.py db upgrade
```

#### Note

If you make changes to the models, you need to create migrations for the changes by running `python manage.py db migrate` and then `python manage.py db upgrade` to add the changes to the database.

### Run Application

Run the application with this command

```bash
flask run
```

### Test the API

Through your browser go to link `localhost:<flask_port>/`.

### Checkout Application Api docs

Through your browser go to link `localhost:<flask_port>/apidocs`.
