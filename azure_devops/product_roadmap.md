# 🚀 Plataforma Inteligente de Control Logístico

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Passed-brightgreen)
![Cobertura](https://img.shields.io/badge/Cobertura-90%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Deploy](https://img.shields.io/badge/Deploy-Render-blue)

---

## 🎯 Resumen Ejecutivo

Plataforma desplegada en producción que simula decisiones operacionales en procesos logísticos críticos, integrando:

* Validación documental
* Control de acceso
* Evaluación de riesgo operacional
* Orquestación de decisiones

👉 API pública + CI/CD + Quality Gate + Deploy en Cloud

---

## 🔗 Accesos en Producción

**🌐 API en producción**
https://intelligent-logistics-control-platform.onrender.com

**📘 Swagger (documentación interactiva)**
https://intelligent-logistics-control-platform.onrender.com/docs

---

## 📸 Evidencia real en producción

### 🌐 API desplegada

![API](docs/api_production.png)

### 📘 Swagger en producción

![Swagger](docs/swagger_production.png)

### ⚙️ Logs de ejecución

![Logs](docs/logs.png)

---

## 👩‍💼 Rol en el proyecto

Este proyecto fue desarrollado desde un enfoque de **Delivery Management**, integrando:

* Definición del enfoque de solución
* Priorización de backlog y roadmap
* Modelamiento del flujo operacional
* Aseguramiento de calidad (testing + CI/CD)
* Enfoque en valor de negocio

---

## 🧩 Problema de Negocio

* Validación manual de documentos
* Ingreso de camiones no autorizados
* Falta de control sobre conductores y vehículos
* Evaluación tardía de riesgos
* Procesos lentos y propensos a error

---

## 📊 Antes vs Después

| Antes                 | Después                  |
| --------------------- | ------------------------ |
| Validaciones manuales | Validación automatizada  |
| Procesos lentos       | Decisiones automatizadas |
| Alto riesgo operativo | Evaluación automatizada  |
| Baja trazabilidad     | Trazabilidad completa    |

---

## 💡 Solución

* ✔ Validación documental
* ✔ Control de acceso
* ✔ Evaluación de riesgo
* ✔ Orquestación de decisiones
* ✔ Generación de tickets
* ✔ Notificaciones

---

## 🏗️ Estructura de la Solución

📊 Flujo operacional:

![Flujo Operacional](diagrams/flujo_operacional_general.png)

📌 Componentes:

```
app/
 ├── api.py
 ├── orchestrator.py
 └── services/
      ├── document_validator.py
      ├── access_control.py
      ├── risk_assessor.py
      ├── ticket_generator.py
      └── notification_service.py
```

---

## 🔄 Flujo de la Solución

1. Recepción de datos
2. Validación documental
3. Evaluación de acceso
4. Análisis de riesgo
5. Decisión
6. Ticket
7. Notificación

---

## 🚨 Escenarios de decisión

* ❌ Documentos faltantes → REJECTED
* ❌ Acceso inválido → REJECTED
* ⚠️ Riesgo alto → REVIEW_REQUIRED
* ✔️ Operación válida → APPROVED

---

## 📸 Evidencia de Ejecución

| Caso                 | Resultado       | Evidencia                             |
| -------------------- | --------------- | ------------------------------------- |
| Documentos faltantes | REJECTED        | ![Caso1](docs/rejected_documents.png) |
| Acceso inválido      | REJECTED        | ![Caso2](docs/rejected_access.png)    |
| Riesgo alto          | REVIEW_REQUIRED | ![Caso3](docs/high_risk.png)          |
| Operación válida     | APPROVED        | ![Caso4](docs/approved.png)           |

---

## 🔌 Endpoints

### Health Check

GET /health

### Evaluación

POST /evaluate

---

## ⚙️ Integración CI/CD y Calidad

Pipeline:

Push → GitHub Actions → Tests → Lint → Coverage → SonarCloud

---

## 📊 Evidencia de Calidad (SonarCloud)

![Quality Gate](docs/sonar_quality_gate.png)

![Coverage](docs/sonar_overview.png)

🔗 https://sonarcloud.io/project/overview?id=vermaldonado-ia_intelligent-logistics-control-platform

---

## ⚙️ Ejecución en Entorno de Desarrollo

```bash
git clone https://github.com/vermaldonado-ia/intelligent-logistics-control-platform.git
cd intelligent-logistics-control-platform
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.api:app --reload
```

🔗 http://127.0.0.1:8000/docs

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

## 📈 Valor para el negocio

* ✔ Reducción de riesgos
* ✔ Automatización
* ✔ Mayor trazabilidad
* ✔ Mejora operativa

---

## 📊 Gestión del Delivery (Azure DevOps)

* ✔ Backlog estructurado
* ✔ Historias y tareas
* ✔ Priorización por valor
* ✔ Kanban
* ✔ Trazabilidad

🔗 [Ver evidencia](./azure_devops/boards_evidencia.md)

---

## 📊 Gestión de Producto

* 📄 [Product Backlog](./product_backlog.md)
* 🚀 [Product Roadmap](./product_roadmap.md)
* 🔗 [Evidencia](./azure_devops/product_backlog.md)

---

## 🚀 Próximos pasos

* ✔ APIs reales
* ✔ IA
* ✔ Arquitectura distribuida
* ✔ IoT

---

## 🎯 Valor diferencial

* ✔ Diseño orientado a negocio
* ✔ Automatización de decisiones
* ✔ DevOps
* ✔ Producción real

👉 Representa un Delivery Manager moderno.

---

## 👩‍💻 Autor

Verónica Maldonado Céspedes
Cloud & DevOps Delivery Manager
