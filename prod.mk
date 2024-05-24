include ./config/.env.production
export $(shell sed 's/=.*//' config/.env.production)

build:
	@docker compose --file docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production build --no-cache

run:
	@docker compose --file docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production up -d

stop:
	@docker compose --file docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production stop

clean_containers:
	@docker container prune --file
    
clean_images:
	@docker image prune --file