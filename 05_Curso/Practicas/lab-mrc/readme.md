# Sistema de Gestión Documental y Calidad

Repositorio del proyecto desarrollado en el marco de las **Prácticas de Ingeniería de Software (Ago–Nov 2025)**. El sistema busca implementar un **control documental y módulos de calidad** alineados con la norma **ISO 15189**, aplicando el ciclo de vida de desarrollo de software (SDLC).

---

## 🚀 Tecnologías
- **Python**
- **FastAPI** (backend REST)
- **PostgreSQL** (base de datos)
- **Docker** (contenedores)
- **Git/GitHub** (control de versiones)

---

## 📂 Estructura del repositorio
```
/docs                → Documentación (SRS, trazabilidad, backlog)
/app                 → Código fuente del backend (FastAPI)
/tests               → Casos de prueba y automatización
/migrations          → Migraciones de base de datos (SQLAlchemy/Alembic)
.dockerfile          → Imagen del backend
requirements.txt     → Dependencias del proyecto
```

---

## 📌 Objetivos
1. Implementar un **módulo documental** con CRUD, versionado y auditoría.  
2. Desarrollar módulos de apoyo: competencias, metrología, riesgos, no conformidades.  
3. Aplicar **trazabilidad de requisitos** (SRS → HU → código → pruebas).  
4. Documentar el sistema siguiendo buenas prácticas de calidad.  

---

## 📋 Documentación
Toda la documentación se encuentra en la carpeta `/docs`:
- `SRS_v0.1.md` → Especificación de requisitos del software.
- `backlog.md` → Backlog del producto y de los sprints.
- `trazabilidad.md` → Matriz de trazabilidad (req ↔ HU ↔ commits ↔ tests).

---

## ⚙️ Configuración inicial
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<usuario>/<repo>.git
   cd <repo>
   ```

2. Crear entorno virtual e instalar dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. Iniciar servicios con Docker:
   ```bash
   docker-compose up -d
   ```

4. Ejecutar la API:
   ```bash
   fastapi dev main.py
   ```

La documentación interactiva estará disponible en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Estado actual
- [x] Entorno configurado (Semana 1–2)  
- [x] Documentación inicial (SRS, backlog, trazabilidad)  
- [ ] Implementación del módulo documental (Sprint 1)  
- [ ] Integración de competencias, metrología y flujos (Sprints 2–4)  
- [ ] Auditorías, riesgos y cumplimiento (Sprints 5–7)  

---

## 📅 Cronograma
El desarrollo sigue el plan de prácticas (8–14 semanas), con entregas parciales en cada sprint y un demo final.

---

