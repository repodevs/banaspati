# Banaspati

Falcon ~ SQLAlchemy's declarative base ~ Docker

---
## Specifications

##### Logic separation

**TODO**

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
##### Inspiration
_This project is inspired from [Flusk](https://github.com/dimmg/flusk.git)_
