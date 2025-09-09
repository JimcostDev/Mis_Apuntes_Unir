# Software Requirements Specification (SRS)
## Sistema de Gestión Documental y Calidad
**Versión:** 0.1  
**Laboratorio MRC**
**Fecha:** 2025-09-09  

---

## 1. Introducción
### 1.1 Propósito
Este documento especifica los requisitos funcionales y no funcionales del sistema a desarrollar en el marco de las prácticas de Ingeniería de Software (ago–nov 2025). El objetivo es implementar un sistema que permita el control documental, trazabilidad y módulos de apoyo alineados a la norma ISO 15189.

### 1.2 Alcance
El sistema permitirá:
- Control documental (subida, descarga, versionado, auditoría).
- Gestión de competencias y equipos de metrología.
- Flujos preanalíticos y registro de no conformidades.
- Generación de reportes y auditorías.
- Seguridad básica con autenticación JWT y RBAC.

### 1.3 Definiciones
- **SRS**: Software Requirements Specification  
- **RBAC**: Role-Based Access Control  
- **JWT**: JSON Web Token  
- **HU**: Historia de usuario  

---

## 2. Descripción general
### 2.1 Usuarios del sistema
- **Administrador**: gestiona usuarios, roles y configuraciones.  
- **Auditor**: revisa documentos y genera reportes.  
- **Técnico**: sube documentos y gestiona calibraciones.  
- **Invitado**: acceso limitado.  

### 2.2 Restricciones
- Backend en **Python + FastAPI**  
- Base de datos en **PostgreSQL**  
- Contenedores con **Docker**  
- Repositorio y control de versiones en **Git**  

---

## 3. Requisitos funcionales
- **R1 — Gestión documental**  
  Subir, editar, descargar y versionar documentos.  

- **R2 — Historial / versionado**  
  Consultar historial de cambios de documentos.  

- **R3 — Auditoría / logs**  
  Registrar todas las operaciones CRUD con usuario, timestamp y motivo.  

- **R4 — Exportar a PDF**  
  Exportar documentos o reportes a PDF con metadatos.  

- **R5 — Autenticación y roles**  
  Acceso mediante JWT, controlado por roles (admin, auditor, técnico, invitado).  

- **R6 — Matriz de competencias**  
  CRUD de competencias, asignación a usuarios y alertas de vencimiento.  

- **R7 — Gestión de equipos y calibraciones**  
  Registrar equipos, planificar calibraciones y generar certificados.  

- **R8 — Flujos preanalíticos**  
  Formularios y validaciones para la admisión de datos.  

- **R9 — Registro de no conformidades**  
  CRUD de NC con estados y acciones correctivas.  

- **R10 — KPIs y auditorías**  
  Definir KPIs y exportar datos para auditorías.  

---

## 4. Requisitos no funcionales
- **NF1 — Seguridad**: JWT + HTTPS + RBAC.  
- **NF2 — Disponibilidad**: uptime mínimo del 99% en horario laboral.  
- **NF3 — Rendimiento**: consultas críticas <500ms con 50 registros.  
- **NF4 — Backup**: respaldo diario y restauración documentada.  
- **NF5 — Trazabilidad**: todo requisito debe mapearse a HUs, commits y pruebas.  

---

## 5. Trazabilidad
Los requisitos se relacionan con historias de usuario, tareas de desarrollo y casos de prueba en el archivo `trazabilidad.md`.

---

## 6. Criterios de aceptación
- Requisitos R1–R5 implementados en el Sprint 1.  
- Documentación técnica (SRS, trazabilidad, manual de despliegue).  
- Demostración de módulos funcionales en la evaluación final.  

---

## 7. Anexos
- Backlog inicial (`backlog.md`).  
- Matriz de trazabilidad (`trazabilidad.md`).  
- Cronograma de sprints.
