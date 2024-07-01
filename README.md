# Perform APP - API | CMS | App

This project is an back-end (api), cms and mobile app for the Perfom Enterprise.

## Lancer le conteneur django en local pour dév

(Il est important d'avoir déjà build les conteneurs dans docker desktop avec la comme `make up_build_dev`)

- Placez-vous dans le dossier backend
- Initiez la commande : poetry config virtualenvs.create false --local
- Installez l'extension "Dev container" sur VSCode
- Exécutez la commande "Open and rebuild container"
- Dans le conteneur vérifiez la version de python avec "which python" et sélectionnez le bon python dans votre config de python debugger
- Sélectionnez l'interpreteur pour Django File
- Lancez le debugger
- Codez dans le conteneur

## Déploiement 

Un github action des plugg

## Installation - DEV

### Build

```bash
make build_dev
```

### Up

```bash
make up_dev
```

### Down

```bash
make down_dev
```

### Make migrations

```bash
make make_migrations_dev
```

### Migrate

```bash
make migrate_dev
```

### Production containers need to be reset (Export db before this !!)

## 1. Stop all containers

```bash
make -f prod.mk stop
```

## 2. Remove all containers

```bash
docker rm -f $(docker ps -a -q)
```

## 3. Remove all volumes

```bash
docker volume rm $(docker volume ls -q)
```

## 4. Prune the system

```bash
docker system prune -a
```

## 5. Restart all containers

```bash
docker compose -f docker-compose.production.yml -p grizzlee-recipes --env-file config/.env.production up -d --build
```

## Lunch python env

When you're currently developping use

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Conventional commit

Start all your commits by "[theme/project] : off the commit".

All projects are :

- [app] : for the mobile app
- [backend] : for the backend
- [cmd] : for the frontend cms

All themes are :

- [fix] : for fix features
- [feat] : for new features
- [wip] : for work in progress
- [docs] : for documentation
- [refactor] : for code refactorization

## Created with

_Languages utilisés :_

- [Django - 4.1](https://www.django-rest-framework.org/) - The best. (back-end)
- [Vue.js](https://vuejs.org/) - An approachable, performant and versatile framework for building web user interfaces.

## Versions

_Versions :_
**Dernière version stable :** 0.0.0
**Dernière version :** 0.0.0
