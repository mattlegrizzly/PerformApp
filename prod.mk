include ./config/.env.production
export $(shell sed 's/=.*//' config/.env.production)

ENV=config/.env.production
API=django

build:
	@docker compose -f docker-compose.production.yml -p perform-app --env-file config/.env.production build --no-cache

run:
	@docker compose -f docker-compose.production.yml -p perform-app --env-file config/.env.production up -d
	@docker cp vue_cms_prod:/var/www/admin/. /var/www/admin

stop:
	@docker compose -f docker-compose.production.yml -p perform-app --env-file config/.env.production stop

clean_containers:
	@docker container prune -f
    
clean_images:
	@docker image prune -f

createsuperuser:
	@docker compose -f docker-compose.production.yml exec $(API) python manage.py createsuperuser

init_db:
	@docker compose -f docker-compose.production.yml --env-file config/.env.production exec -u $(DB_USER) postgres psql $(DB_NAME) $(DB_USER) -f /docker-entrypoint-initdb.d/init.sql