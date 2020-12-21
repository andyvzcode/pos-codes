# Test mi Aguila



Development by [Andres Vasquez](https://github.com/anfevazu)

## Descripcion del proyecto

Servicios para alimentar la base de datos de viajes

## Tecnologias del proyecto

- Python 3.6
- Django - GeoDjango => 3.0.6
- Docker => 19.03.8
- Compose => 1.25.5
- postgres => 11
- postgis => 2.5.1 r17027
- Docker Image => python:3.6
- GDAL => last version


## Ramas del proyecto
- master

## Comando para levantar el proyecto
```bash
$ docker-compose -f compose/development.yml up --build
```


## Urls del proyecto
- Administrador : http://localhost:81/admin
-- usuario : admin -- password: 123456
- Api Root : http://localhost:81/api/v1
- Load Json file : http://localhost:81/api/v1/upload
