ENV_FILE = $(shell pwd)$(shell echo '/.env')

include $(ENV_FILE)
export $(shell sed 's/=.*//' `pwd`/.env)

_DEVELOPMENT_DATABASE_URI=$(DEVELOPMENT_DATABASE_URI)
_TEST_DATABASE_URI=$(TEST_DATABASE_URI)

.PHONY: clear run-server help dcompose-start dcompose-start dcompose-stop dcleanup

clear:
	@find . -name __pycache__ -prune -exec rm -rf {} +
	@find . -name "*.pyc" -prune -exec rm -rf {} +
	@find . -name .cache -prune -exec rm -rf {} +

db-revision:
	@(\
		cd core/migrations && alembic revision --autogenerate -m "$(msg)"; \
	)

db-upgrade:
	@(\
	    cd core/migrations && alembic upgrade head \
	)

db-upgrade-sql:
	@(\
		cd core/migrations && alembic upgrade head --sql; \
	)

db-downgrade:
	@(\
	    cd core/migrations && alembic downgrade -1 \
	)


dcompose-start:
	@docker-compose stop;
	@docker-compose build;
	@docker-compose up -d;

dcompose-restart:
	@docker-compose stop;
	@docker-compose build;
	@docker-compose up -d;

dcompose-stop:
	@docker-compose stop

dcleanup:
	@docker rm $(docker ps -qa --no-trunc --filter "status=exited")
	@docker rmi $(docker images --filter "dangling=true" -q --no-trunc)

run-server:
	@(\
		export SQLALCHEMY_DATABASE_URI=$(_DEVELOPMENT_DATABASE_URI); \
		gunicorn core.wsgi:app -w 1 --bind "0.0.0.0:8338" --reload\
	)

run-tests: clear
	@(\
		export SQLALCHEMY_DATABASE_URI=$(_TEST_DATABASE_URI); \
		pytest -s --disable-warnings; \
	)

help:
	@echo 'dcompose-start:'
	@echo '	Build and start containers'
	@echo 'dcompose-stop:'
	@echo '	Stop running containers'
	@echo 'dcleanup:'
	@echo '	Remove docker containers with status `exited`'
	@echo '	Remove unused docker images'
	@echo 'run-server:'
	@echo '	Start application server'
	@echo 'run-tests:'
	@echo '	Run tests'
	@echo 'clear:'
	@echo '	Remove *.pyc files, __pycache__ and .cache folders'
	@echo 'db-revision:'
	@echo '	Create database migrations using alembic'
	@echo 'db-upgrade:'
	@echo '	Apply migrations using alembic'
	@echo 'db-upgrade-sql:'
	@echo '	Show DDL migrations'
	@echo 'db-downgrade:'
	@echo '	Downgrade 1 migrations'
