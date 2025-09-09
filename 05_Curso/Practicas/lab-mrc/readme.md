# Sistema de Gestión Documental y Calidad

Repositorio del proyecto desarrollado en el marco de las **Prácticas de Ingeniería de Software (Ago–Nov 2025)**. El sistema busca implementar un **control documental y módulos de calidad** alineados con la norma **ISO 15189**, aplicando el ciclo de vida de desarrollo de software (SDLC).

> [!NOTE]
> Este proyecto está basado en el template de FastAPI + PostgreSQL, adaptado específicamente para sistemas de gestión documental y calidad.

> [!TIP]
> La documentación interactiva de la API estará disponible en `/docs` una vez que el servidor esté ejecutándose.

## 📂 Estructura del repositorio

El proyecto sigue una **arquitectura en capas** para promover la separación de responsabilidades y facilitar la mantenibilidad y escalabilidad, adaptada específicamente para sistemas de gestión documental.

```
api/                    → Controladores (routers) - endpoints de la API
services/               → Lógica de negocio y orquestación  
repositories/           → Patrón Repositorio - acceso a datos
models/                 → Modelos de datos y validación
core/                   → Configuración, conexión DB, autenticación
utils/                  → Funciones de utilidad reutilizables
tests/                  → Suite de pruebas unitarias e integración
docs/                   → Documentación (SRS, trazabilidad, backlog)
main.py                 → Punto de entrada de la aplicación FastAPI
requirements.txt        → Dependencias del proyecto
```

---

## 🚀 Tecnologías
- **Python** - Lenguaje principal
- **FastAPI** - Framework para API REST
- **PostgreSQL** - Base de datos relacional
- **SQLAlchemy + asyncpg** - ORM y conexión asíncrona
- **Docker** - Contenedores
- **Git/GitHub** - Control de versiones
- **Pytest** - Framework de testing

---


## 📌 Objetivos
1. Implementar un **módulo documental** con CRUD, versionado y auditoría
2. Desarrollar módulos de apoyo: competencias, metrología, riesgos, no conformidades
3. Aplicar **trazabilidad de requisitos** (SRS → HU → código → pruebas)
4. Documentar el sistema siguiendo buenas prácticas de calidad
5. Cumplir con lineamientos de la norma **ISO 15189**

---

## ⚙️ Configuración inicial

> [!IMPORTANT]  
> Debes configurar correctamente las variables de entorno en tu archivo `core/config.env` o exportarlas en tu sistema.

### 1. **Clona este repositorio**:
```bash
git clone https://github.com/<usuario>/<repo>.git
cd <repo>
```

### 2. **Crea y activa tu entorno virtual**:
- Crear entorno virtual:
    ```bash
    python -m venv venv
    ```
- Activar el entorno virtual:
    - En **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - En **macOS y Linux**:
        ```bash
        source venv/bin/activate
        ```

### 3. **Instala las dependencias requeridas**:
```bash
pip install -r requirements.txt
```

### 4. **Configuración de Base de Datos PostgreSQL**:
```sh
# core/config.env
POSTGRES_URI=postgresql+asyncpg://user:password@localhost:5432/db_name
JWT_SECRET_KEY=secreto-muy-secreto-para-gestion-documental
DB_ENGINE=postgresql
```

### 5. **Iniciar servicios con Docker**:
```bash
docker-compose up -d
```

### 6. **Ejecutar migraciones de base de datos**:
```bash
alembic upgrade head
```

### 7. **Ejecuta el servidor**:
- Modo **desarrollo**:
    ```bash
    fastapi dev main.py
    ```
- Modo **producción**:
    ```bash
    fastapi run
    ```

La documentación interactiva estará disponible en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📋 Documentación
Toda la documentación se encuentra en la carpeta `/docs`:
- `SRS_v0.1.md` → Especificación de requisitos del software
- `backlog.md` → Backlog del producto y de los sprints
- `trazabilidad.md` → Matriz de trazabilidad (req ↔ HU ↔ commits ↔ tests)

---

## ✅ Estado actual
- [x] Entorno configurado (Semana 1–2)
- [x] Documentación inicial (SRS, backlog, trazabilidad)
- [x] Template base de FastAPI adaptado
- [ ] Implementación del módulo documental (Sprint 1)
- [ ] Integración de competencias, metrología y flujos (Sprints 2–4)
- [ ] Auditorías, riesgos y cumplimiento (Sprints 5–7)

---

## 📅 Cronograma
El desarrollo sigue el plan de prácticas (8–14 semanas), con entregas parciales en cada sprint y un demo final.

### Sprints Planificados:
- **Sprint 1-2**: Módulo documental base
- **Sprint 3-4**: Competencias y metrología
- **Sprint 5-6**: Gestión de riesgos y no conformidades
- **Sprint 7**: Auditorías y reportes finales

---

## 🧪 Testing
Ejecutar la suite completa de pruebas:
```bash
pytest
```

Ejecutar pruebas con coverage:
```bash
pytest --cov=. tests/
```

---

## 🐛 Debugging y Desarrollo
Para desarrollo local con recarga automática:
```bash
fastapi dev main.py
```

---

> [!TIP]  
> ¡Si te resulta útil este proyecto, apóyalo con una ⭐! Tu apoyo nos motiva a crear más contenido y mejorar los recursos disponibles para sistemas de gestión documental. ¡Gracias! :octocat: