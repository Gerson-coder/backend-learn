# backend-learn

Repositorio personal para aprender Python con enfoque en desarrollo backend.

## Objetivo

Construir una base sólida para pasar de soporte técnico a backend developer junior, usando Python como stack principal y desarrollando proyectos reales con APIs, bases de datos, autenticación, testing y deploy.

## Roadmap Backend con Python

> La versión visual e interactiva está en: [`ruta-backend-python.html`](./ruta-backend-python.html)

### Nivel 1 — Fundamentos de Python

- Variables y tipos de datos
- Input/output
- Operadores
- Condicionales
- Bucles
- Funciones
- `main()` y `if __name__ == "__main__"`
- PEP 8 inicial

### Nivel 2 — Estructuras de datos y código reusable

- Listas
- Diccionarios
- Tuplas
- Sets
- Módulos y paquetes
- Manejo de errores
- Archivos y JSON
- Typing básico
- `lambda`
- `sorted(key=...)`
- `map` / `filter`
- List comprehensions

### Nivel 3 — Herramientas profesionales

- Entornos virtuales con `venv`
- `pip` y `requirements.txt`
- Variables de entorno
- Git y GitHub
- Terminal/Linux básico
- `pytest` inicial

### Nivel 4 — Async/Await en Python

- `async def` vs `def`
- `await`
- Event loop
- Concurrencia vs paralelismo
- `asyncio` básico
- Código bloqueante vs no bloqueante

### Nivel 5 — HTTP, REST y FastAPI

- Request/response
- Headers
- Status codes
- JSON
- Métodos HTTP
- Diseño REST profesional
- Versionado `/api/v1`
- FastAPI básico
- Pydantic
- OpenAPI / Swagger
- Uso de Postman

### Nivel 6 — Testing de APIs reales

- Tests de endpoints
- `TestClient`
- `httpx`
- `pytest-asyncio`
- Fixtures
- Tests de login
- Tests de permisos
- Tests con base de datos de prueba

### Nivel 7 — Bases de datos

- SQL básico/intermedio
- PostgreSQL
- Relaciones
- Foreign keys
- Índices
- Transacciones
- SQLAlchemy sync
- Alembic
- SQLAlchemy async
- `asyncpg`

### Nivel 8 — Autenticación, autorización y seguridad

- Register/login
- Hashing con `bcrypt`
- JWT access token
- Refresh token
- Cookies `HttpOnly`
- `Secure`
- `SameSite`
- Roles y permisos
- CORS
- CSRF
- SQL injection
- Rate limiting

### Nivel 9 — Arquitectura backend

- Routes
- Services
- Repositories
- Schemas
- Service Layer
- Repository Pattern
- Dependency Injection
- DTO / Schemas
- Factory básico
- Strategy básico
- Adapter básico
- Unit of Work
- Documentación técnica

### Nivel 10 — Producción, Docker y deploy

- Dockerfile
- Docker Compose
- Variables por ambiente
- Uvicorn/Gunicorn
- Nginx básico
- Health checks
- Logs
- Deploy en Render/Railway/Fly.io
- GitHub Actions
- Backups básicos
- Secrets
- Monitoreo básico

### Nivel 11 — Extras para destacar

- Redis
- Cache
- Rate limiting avanzado
- Celery o RQ
- Background jobs
- Emails
- Webhooks
- Procesamiento de archivos
- APIs externas

### Nivel 12 — Proyecto final profesional

Proyecto recomendado:

**API de gestión de tickets técnicos**

Debe incluir:

- Usuarios
- Login/logout
- JWT en cookies
- Roles: admin, operador, usuario
- CRUD de tickets
- Estados y prioridades
- Comentarios
- Filtros
- PostgreSQL
- SQLAlchemy
- Alembic
- Tests de endpoints
- Docker
- Deploy
- README profesional
- Swagger público

## Estructura actual

```txt
backend-learn/
├── assets/
│   ├── app.js
│   └── styles.css
├── nivel-1/
├── nivel-2/
├── nivel3/
├── notas/
├── niveles.md
├── ruta-backend-python.html
└── README.md
```

## Regla principal

No estudiar temas en abstracto. Cada bloque debe terminar en código, ejercicios, tests o una feature explicable.
