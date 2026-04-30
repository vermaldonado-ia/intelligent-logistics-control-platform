# 🚛 Intelligent Logistics Control Platform

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Passed-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-85%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)

---

## 🌐 API en Producción

🔗 API en producción:
https://intelligent-logistics-control-platform.onrender.com

📘 Swagger (documentación interactiva):
https://intelligent-logistics-control-platform.onrender.com/docs

✔ Deploy automático desde GitHub
✔ API pública accesible
✔ Documentación interactiva
✔ Runtime en cloud

⚠️ Nota: al estar en free tier, puede tardar unos segundos en iniciar.

---

## 📸 Evidencia real en producción

🌐 API desplegada en Render
📘 Swagger en producción
⚙️ Logs de ejecución

---

## 🧠 Descripción

Plataforma desplegada en producción que simula decisiones operacionales en procesos logísticos críticos, integrando:

* Validación documental
* Control de acceso
* Análisis de riesgo operacional

Permite simular un flujo real de decisión automatizada en entornos logísticos complejos.

---

## 🎯 Objetivo

Diseñar una solución tecnológica orientada a negocio que permita:

* Reducir riesgos operacionales
* Disminuir errores manuales
* Mejorar tiempos de validación
* Aumentar trazabilidad y control

---

## 🧩 Problema de Negocio

En operaciones logísticas reales existen múltiples puntos críticos:

* Validación manual de documentos
* Ingreso de camiones no autorizados
* Falta de control sobre conductores y vehículos
* Evaluación tardía de riesgos operacionales
* Procesos lentos y propensos a error

👉 Impacto directo:

* Seguridad operativa
* Continuidad del servicio
* Trazabilidad
* Eficiencia del proceso

---

## 📊 Antes vs Después

| Antes                 | Después                           |
| --------------------- | --------------------------------- |
| Validaciones manuales | Validación automatizada           |
| Procesos lentos       | Decisiones automatizadas          |
| Alto riesgo operativo | Evaluación automatizada de riesgo |
| Baja trazabilidad     | Trazabilidad completa             |

---

## 💡 Solución

Se desarrolló una API que simula un motor de decisiones inteligente, capaz de:

✔ Validar documentación
✔ Evaluar condiciones de acceso
✔ Analizar riesgo operacional
✔ Orquestar decisiones
✔ Generar tickets de acceso
✔ Emitir notificaciones

---

## 🏗️ Arquitectura de la solución

```
app/
├── api.py
├── orchestrator.py
└── services/
```

* API Layer → exposición de endpoints (FastAPI)
* Orchestration Layer → lógica de decisión central
* Services Layer → reglas de negocio desacopladas

👉 Permite:

* Escalabilidad
* Mantenibilidad
* Separación de responsabilidades
* Evolución hacia microservicios

---

## 🧠 Enfoque del Proyecto

Proyecto diseñado desde una perspectiva de Delivery y negocio:

✔ Modelamiento de decisiones reales
✔ Orquestación de reglas
✔ Simulación de escenarios críticos
✔ Outputs trazables y explicables

---

## 🔄 Flujo de la Solución

1. Recepción de datos
2. Validación documental
3. Evaluación de acceso
4. Análisis de riesgo
5. Toma de decisión
6. Generación de ticket
7. Notificación

📌 Ver diagrama:
👉 diagrams/flujo_operacional_general.png

---

## 🚨 Escenarios de decisión

❌ Documentos faltantes → REJECTED
❌ Documento expirado → REJECTED
⚠ Riesgo alto → REVIEW_REQUIRED
✔ Operación válida → APPROVED

---

## 📸 Evidencia de ejecución (Swagger)

| Caso                 | Resultado       | Evidencia                             |
| -------------------- | --------------- | ------------------------------------- |
| Documentos faltantes | REJECTED        | ![Caso1](docs/rejected_documents.png) |
| Acceso inválido      | REJECTED        | ![Caso2](docs/rejected_access.png)    |
| Riesgo alto          | REVIEW_REQUIRED | ![Caso3](docs/high_risk.png)          |
| Operación válida     | APPROVED        | ![Caso4](docs/approved.png)           |

---

## 🔌 Endpoints

### ✔ Root (API en producción)

GET /

```json
{
  "message": "Intelligent Logistics Control Platform API",
  "status": "running",
  "docs": "/docs",
  "health": "/health"
}
```

👉 Permite validar que la API está operativa en producción.

---

### ✔ Health Check

GET /health

```json
{"status": "ok"}
```

---

### ✔ Evaluación de Operación

POST /evaluate

```json
{
  "payload": {
    "driver": {
      "authorized": true,
      "fatigue_level": "medium"
    },
    "vehicle": {
      "authorized": true
    },
    "cargo": {
      "type": "container",
      "declared_value": 120000
    }
  }
}
```

---

## 🧪 Pruebas y Calidad

```bash
pytest -v
pytest --cov=app
```

✔ CI con GitHub Actions
✔ Validación con SonarCloud
✔ Control de cobertura

---

## ⚙️ Tecnologías

* Python
* FastAPI
* Pytest
* Flake8
* Coverage
* GitHub Actions
* SonarCloud

---

## ⚙️ CI/CD y Calidad

Flujo:

Push → GitHub Actions → Tests → Lint → Coverage → SonarCloud

✔ Quality Gate: Passed
✔ Coverage: ~85%
✔ Maintainability: A
✔ Reliability: A
✔ Security: A

---

## 🚀 Ejecución local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.api:app --reload
```

Swagger:
http://127.0.0.1:8000/docs

---

## 📈 Valor para el negocio

✔ Reducción de riesgos
✔ Automatización
✔ Trazabilidad
✔ Eficiencia operacional
✔ Base para evolución tecnológica

---

## 🚀 Próximos pasos

✔ Integración con APIs reales
✔ IA para scoring de riesgo
✔ Arquitectura distribuida
✔ IoT (GPS, sensores)

---

## 🎯 Valor diferencial del proyecto

✔ Diseño orientado a negocio
✔ Modelamiento real
✔ Automatización de decisiones
✔ CI/CD + Deploy
✔ API en producción

👉 Representa el rol de un Delivery Manager moderno

---

## 🚀 Estrategia de Desarrollo

MVPs incrementales

### MVP1 — Validación del Flujo Operacional

Validación completa del flujo en entorno simulado

---

## 🎯 Visión del Producto

Automatizar decisiones logísticas con foco en:

* Trazabilidad
* Control
* Reducción de riesgos

---

## 📊 Gestión del Delivery

Gestionado con Azure DevOps:

✔ Backlog
✔ Historias
✔ Tareas
✔ Priorización
✔ Kanban
✔ Trazabilidad

---

## 📎 Evidencia Azure DevOps

👉 ./azure_devops/boards_evidencia.md

---

## 📊 Gestión de Producto

* 📄 Product Backlog
* 🚀 Product Roadmap
* 🔗 Evidencia Boards

---

## 👩‍💻 Autor

**Verónica Maldonado Céspedes**
Cloud & DevOps Delivery Manager
Project Manager | Transformación Digital

---

