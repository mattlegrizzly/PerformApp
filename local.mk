include ./config/.env.local
export $(shell sed 's/=.*//' config/.env.local)

API=django
CMP=docker-compose.local.yml
ENV=config/.env.local
PRJ=perform_cms_local

build:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) build

build_no_cache:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) build --no-cache

up_build:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) up -d --build

up:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) up -d

stop:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) stop
	
down:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) down

down_volumes:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) down -v

make_migrations:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(API) python manage.py makemigrations

migrate:
	@docker compose -f $(CMP) --env-file $(ENV) exec $(API) python manage.py migrate
	
createsuperuser:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) exec $(API) python manage.py createsuperuser

init_db:
	@docker compose -f $(CMP) -p $(PRJ) --env-file $(ENV) exec -u $(DB_USER) postgres psql $(DB_NAME) $(DB_USER) -f /docker-entrypoint-initdb.d/init.sql