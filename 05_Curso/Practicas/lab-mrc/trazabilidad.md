# Matriz de Trazabilidad, v0.1

| Req ID | Descripción | Historia de Usuario | Sprint | Commit/Branch | Test Case |
|--------|-------------|---------------------|--------|---------------|-----------|
| R1 | Gestión documental | HU-01 | Sprint 1 | feat/docs-crud | TC-01 |
| R2 | Historial / versionado | HU-02 | Sprint 1 | feat/docs-history | TC-02 |
| R3 | Auditoría / logs | HU-05 | Sprint 1 | feat/docs-audit | TC-03 |
| R4 | Exportar a PDF | HU-04 | Sprint 1 | feat/pdf-export | TC-04 |
| R5 | Autenticación y roles | HU-03 | Sprint 13 (auth básica en Sprint 1) | feat/auth-jwt | TC-05 |
| R6 | Matriz de competencias | HU-06 | Sprint 2 | feat/competencias | TC-06 |
| R7 | Gestión de equipos y calibraciones | HU-07 | Sprint 3 | feat/equipos-cal | TC-07 |
| R8 | Flujos preanalíticos | HU-08 | Sprint 4 | feat/preanaliticos | TC-08 |
| R9 | Registro de no conformidades | HU-09 | Sprint 5 | feat/nc-registro | TC-09 |
| R10 | KPIs y auditorías | HU-10 | Sprint 6 | feat/kpis | TC-10 |
| R11 | Matriz de riesgos y proveedores | HU-11 | Sprint 7 | feat/riesgos-proveedores | TC-11 |
| R12 | Backups y bitácoras | HU-12 | Sprint 13 | feat/backups-logs | TC-12 |

---

## ¿Qué es la trazabilidad?

En ingeniería de software, la **trazabilidad** es la capacidad de seguir el rastro de un requisito desde que se define hasta que se cumple. Permite demostrar que **todo lo que se especificó en el SRS** fue implementado, probado y entregado.

Se representa como un **mapa de relaciones**:

- **Requisito (SRS)** → **Historia de usuario (backlog)** → **Commit/Rama (código)** → **Caso de prueba (testing)** → **Entrega (release)**

Ejemplo:
- **R3 — Auditoría/logs**
  - SRS: Requisito R3
  - Historia de usuario: HU-05
  - Rama: `feat/docs-audit`
  - Commit: `R3: agregar auditoría de documentos (HU-05)`
  - Test case: TC-03

De esta manera, si un auditor pregunta *“¿Dónde se implementa el requisito R3?”*, puedes rastrear la relación completa.

---

## ¿Para qué sirve?
1. **Evidencia**: demuestras que cada requisito fue atendido.  
2. **Orden**: evitas perder de vista funcionalidades importantes.  
3. **Auditoría**: fundamental en normas como ISO 15189.  
4. **Mantenimiento**: si un requisito cambia, sabes qué código y test actualizar.

---

## Tips para crear trazabilidad
- **Commits claros**:  
  `R1: agregar endpoint de subida de documentos (HU-01)`

- **Branches por feature**:  
  `feat/R1-docs-crud`

- **Issues/tickets con IDs**: cada requisito o HU tiene su issue vinculado.

- **Matriz simple**: tabla con Req ID ↔ HU ↔ Commit ↔ Test.
