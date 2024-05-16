DOMAIN?=perform_cms.fr
PACKAGE?=
WIN_HOSTS_PATH=/mnt/c/Windows/System32/drivers/etc/hosts
WSL_HOSTS_PATH=/etc/hosts

build_dev:
	@make -f dev.mk build

build_no_cache_dev:
	@make -f dev.mk build_no_cache

up_build_dev:
	@make -f dev.mk up_build

up_dev:
	@make -f dev.mk up

stop_dev:
	@make -f dev.mk stop

down_dev:
	@make -f dev.mk down

down_volumes_dev:
	@make -f dev.mk down_volumes

add_package_admin_dev:
	@make -f dev.mk add_package_admin PACKAGE=$(PACKAGE)

add_package_client_dev:
	@make -f dev.mk add_package_client PACKAGE=$(PACKAGE)

make_migrations_dev:
	@make -f dev.mk make_migrations

migrate_dev:
	@make -f dev.mk migrate

create_superuser_dev:
	@make -f dev.mk create_superuser

init_db_dev:
	@make -f dev.mk init_db

build_local:
	@make -f local.mk build

build_no_cache_local:
	@make -f local.mk build_no_cache

up_build_local:
	@make -f local.mk up_build

up_local:
	@make -f local.mk up

stop_local:
	@make -f local.mk stop

down_local:
	@make -f local.mk down

down_volumes_local:
	@make -f local.mk down_volumes

make_migrations_local:
	@make -f local.mk make_migrations

migrate_local:
	@make -f local.mk migrate

createsuperuser_local:
	@make -f local.mk createsuperuser

init_db_local:
	@make -f local.mk init_db

clean_all:
	@docker system prune -a -f

clean_volumes:
	@docker volume prune -v -f

containers:
	@docker ps -a

wsl_etc_show:
	@cat $(WSL_HOSTS_PATH)

wsl_etc_edit:
	@sudo nano $(WSL_HOSTS_PATH)

win_etc_show:
	@cat $(WIN_HOSTS_PATH)