# Perform APP - API | CMS | App

This project is an back-end (api), cms and mobile app for the Perfom Enterprise.

## Installation

### Build

```bash
make build
```

### Up

```bash
make up
```

### Down

```bash
make down
```

### Make migrations

```bash
make makemigrate
```

### Migrate

```bash
make migrate
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

## Authors

- **Mattéo ANDRE** _Developper_ (<https://github.com/mattlegrizzly>)