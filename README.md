# pc-automation-server
PC Automation Server

## Run with docker

### Create network and volume
```bash
docker network create lambo-net
```
```bash
docker volume create lambo-data
```

### Run mysql and redis
```bash
docker run -d --network lambo-net --network-alias redis redis/redis-stack-server
```
```bash
docker run -d --network lambo-net --network-alias mysql -v lambo-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=pcautomations mysql:5.7
```

### Run pc-automation-server
```bash
docker run -dp 8281:80 --network lambo-net -v lambo-data:/app/media fshangala/pc-automation-server:main
```

## Run with docker compose
```bash
docker-compose up -d
```
or
```bash
docker compose up -d
```

## Apply migrations and create superuser
```bash
docker exec -it <container_id> /bin/bash
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser --username admin --email admin@localhost
```