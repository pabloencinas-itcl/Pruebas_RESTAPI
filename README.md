# TravelHub

TravelHub es una API sencilla para gestionar reservas de viajes (vuelos y hoteles),
destinos y usuarios. Pensado como proyecto de ejemplo con una arquitectura en capas
clásica:

```
api/         -> capa de presentación (rutas HTTP, entrada/salida)
services/    -> capa de lógica de negocio (casos de uso)
database/    -> capa de acceso a datos (modelos + repositorios)
schemas/     -> validación y serialización de datos (Pydantic-like)
core/        -> configuración, seguridad y excepciones transversales
utils/       -> funciones auxiliares genéricas, sin lógica de negocio
scripts/     -> utilidades de mantenimiento fuera del flujo de la API
tests/       -> pruebas unitarias
```

## Arquitectura

Este proyecto sigue una **arquitectura en capas (layered architecture)**:

`api -> services -> database`

- La capa `api` no debe conocer detalles de la base de datos.
- La capa `services` contiene la lógica de negocio y orquesta los repositorios.
- La capa `database` implementa el **patrón Repository**, aislando el acceso a datos
  para que `services` no dependa de SQL ni de un ORM concreto.

## Instalación

```bash
pip install -r requirements.txt
python main.py
```
