# Banaspati

[![Build Status](https://travis-ci.org/repodevs/banaspati.svg?branch=master)](https://travis-ci.org/repodevs/banaspati)

Robust web API powered by Falcon, SQLAlchemy and Docker

---
## Specifications

##### Tech Stack
- Falcon
- SQLAlchemy (declarative base)
- Alembic
- Docker


##### Logic separation

**TODO**

---
## Directory Layout

```
.
├── Dockerfile
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── core
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── book
│   │   │   ├── __init__.py
│   │   │   ├── backend.py
│   │   │   ├── domain.py
│   │   │   ├── models.py
│   │   │   └── resource.py
│   │   ├── common
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   ├── exceptions.py
│   │   │   ├── middleware
│   │   │   │   ├── __init__.py
│   │   │   │   ├── context.py
│   │   │   │   ├── request.py
│   │   │   │   └── response.py
│   │   │   ├── serializers.py
│   │   │   └── utils.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       └── book
│   │           ├── __init__.py
│   │           ├── create_book.json
│   │           └── update_book.json
│   ├── migrations
│   │   ├── __init__.py
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 8d0c7114a367_init_book_api.py
│   │       └── __init__.py
│   ├── routes.py
│   └── wsgi.py
├── deployment
│   ├── nginx
│   │   ├── Dockerfile
│   │   └── sites-enabled
│   │       └── banaspati.conf
│   └── postgres
│       ├── Dockerfile
│       └── sql
│           └── init.sql
└── docker-compose.yml
```

## Installation
#### Install dependencies

```
$ pipenv install
```

#### Settings configuration
Settings configuration by creating `.env` file on root project
```
$ cp .env.example .env
```

Edit file and change the params

#### Apply Migration
```
$ make db-upgrade
```

#### Run Application
```
$ make run-server
```

---
#### Run App with docker

##### Build Image
```
$ docker build -t repodevs/banaspati:1.0 .
```

##### Create containers
```
$ docker run -d --name banaspati-dev -e "SQLALCHEMY_DATABASE_URI=postgres://banaspatidbuser@db:5432/banaspatidev" --link postgres-banaspati:db -p 8338:8338 repodevs/banaspati:1.0
```
**NOTE: _Need database (postgres) to run_**

---
#### Run with docker-compose
##### Build and run containers
```
$ docker-compose up -d --build
```

##### Migrate database
```
$ docker exec banaspati-api bash -c "cd core/migrations && alembic upgrade head"
```

---
## Available REST API

I use `HTTPie` to test via CLI, Have you try it? :)

#### Create Book
```
$ http POST http://0.0.0.0:8338/book author="Edi Santoso" name="Falcon Book" isbn:=8338
```

#### Get Book Detail
```
$ http GET http://0.0.0.0:8338/book/{BOOK_ID}
```

#### Update Book
```
$ http PUT http://0.0.0.0:8338/book/{BOOK_ID} name="Falcon Book for Beginer" isbn:=18338
```

#### Delete Book
```
$ http DELETE http://0.0.0.0:8338/book/{BOOK_ID}
```

#### Get All Books
```
$ http GET http://0.0.0.0:8338/books
```

---
##### Inspiration
_This project is inspired from [Flusk](https://github.com/dimmg/flusk.git)_
