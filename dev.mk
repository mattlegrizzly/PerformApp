include ./config/.env.dev
export $(shell sed 's/=.*//' .env)

ADMIN=react_admin
API=django_dev
CLIENT=react_client
CMP=docker-compose.dev.yml
ENV=.env
PACKAGE?=

build:
	@docker compose -f $(CMP) --env-file $(ENV) build 

build_no_cache:
	@docker compose -f $(CMP) --env-file $(ENV) build --no-cache

up_build:
	@docker compose -f $(CMP) --env-file $(ENV) up -d --build

up:
	@docker compose -f $(CMP) --env-file $(ENV) up -d && make -f dev.mk run_django

stop:
	@docker compose -f $(CMP) --env-file $(ENV) stop

down:
	@docker compose -f $(CMP) --env-file $(ENV) down

down_volumes:
	@docker compose -f $(CMP) --env-file $(ENV) down -v

add_package_admin:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(ADMIN) npm install $(PACKAGE)
	
add_package_client:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(CLIENT) npm install $(PACKAGE)

make_migrations:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(API) python manage.py makemigrations

migrate:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(API) python manage.py migrate

create_superuser:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(API) python manage.py createsuperuser

init_db:
	@docker compose -f $(CMP) --env-file $(ENV) exec postgres psql $(DB_NAME) $(DB_USER) -f /docker-entrypoint-initdb.d/init.sql

run_django:
	@docker exec -d $(API) python manage.py runserver 0.0.0.0:8000