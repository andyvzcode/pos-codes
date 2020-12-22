# Test mi Aguila

Development by [Andres Vasquez](https://github.com/anfevazu)

## Descripcion del proyecto

Servicios para validar codigos de area de unas cordenadas especificas

## Tecnologias del proyecto

- Python
- Django
- Docker
- Compose
- postgres
- Docker Image => python:3.8
- SQLite

## Ramas del proyecto

- master

## Comando para levantar el proyecto

```bash
$ docker-compose  up --build
```

## Urls del proyecto

- Healt services : http://localhost:90/api/healthcheck - http://localhost:90/api/healthcheck
- Load File : http://localhost:90/api/load-file
- Process File : http://localhost:91/api/process-file

## Cuando se ejecuta el servico de cargar archivo este a su vez llama el servicio de procesar archivo a traves de la red de docker.
