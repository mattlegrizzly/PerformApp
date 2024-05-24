include ./config/.env.production
export $(shell sed 's/=.*//' config/.env.production)

build:
	@docker compose -f docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production build --no-cache

run:
	@docker compose -f docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production up -d

stop:
	@docker compose -f docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production stop

clean_containers:
	@docker container prune -f
    
clean_images:
	@docker image prune -f