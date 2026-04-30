# 🚛 Intelligent Logistics Control Platform

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Passed-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-85%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)

---

## 🌐 Accesos en Producción

🔗 **API en producción**
👉 https://intelligent-logistics-control-platform.onrender.com

🔗 **Swagger (documentación interactiva)**
👉 https://intelligent-logistics-control-platform.onrender.com/docs

✔ Deploy automático desde GitHub
✔ API pública accesible
✔ Documentación interactiva
✔ Runtime en cloud

⚠️ Nota: al estar en free tier, puede tardar unos segundos en iniciar.

---

## 📸 Evidencia real en producción

🌐 **API desplegada en Render**
👉 https://intelligent-logistics-control-platform.onrender.com

📘 **Swagger en producción**
👉 https://intelligent-logistics-control-platform.onrender.com/docs

⚙️ **Logs de ejecución (Render)**
👉 https://dashboard.render.com/

---

## 🧠 Descripción

Plataforma desplegada en producción que simula decisiones operacionales en procesos logísticos críticos, integrando:

* Validación documental
* Control de acceso
* Análisis de riesgo operacional

---

## 🎯 Objetivo

* Reducir riesgos operacionales
* Disminuir errores manuales
* Mejorar tiempos de validación
* Aumentar trazabilidad

---

## 🧩 Problema de Negocio

* Validación manual
* Ingreso no autorizado
* Falta de control
* Evaluación tardía
* Procesos lentos

👉 Impacto: seguridad, continuidad, eficiencia

---

## 📊 Antes vs Después

| Antes            | Después      |
| ---------------- | ------------ |
| Manual           | Automatizado |
| Lento            | Rápido       |
| Riesgoso         | Controlado   |
| Sin trazabilidad | Trazable     |

---

## 💡 Solución

API que simula un motor de decisiones:

✔ Validación
✔ Acceso
✔ Riesgo
✔ Orquestación
✔ Ticketing
✔ Notificación

---

## 🏗️ Arquitectura

📌 **Ver diagrama**
👉 ./diagrams/flujo_operacional_general.png

---

## 🔄 Flujo

1. Input
2. Validación
3. Acceso
4. Riesgo
5. Decisión
6. Ticket
7. Notificación

---

## 🚨 Escenarios

❌ REJECTED
⚠ REVIEW_REQUIRED
✔ APPROVED

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

### ✔ API Root (Producción)

👉 https://intelligent-logistics-control-platform.onrender.com

```json
{
  "message": "Intelligent Logistics Control Platform API",
  "status": "running",
  "docs": "/docs",
  "health": "/health"
}
```

---

### ✔ Health Check

👉 https://intelligent-logistics-control-platform.onrender.com/health

---

### ✔ Swagger

👉 https://intelligent-logistics-control-platform.onrender.com/docs

---

## 🧪 Calidad

✔ CI
✔ Coverage
✔ SonarCloud

📊 **Ver análisis**
👉 https://sonarcloud.io/

---

## 🚀 Ejecución local

```bash
pip install -r requirements.txt
python -m uvicorn app.api:app --reload
```

---

## 📊 Gestión del Delivery

👉 **Azure DevOps (evidencia real)**
👉 ./azure_devops/boards_evidencia.md

👉 **Backlog**
👉 ./product_backlog.md

👉 **Roadmap**
👉 ./product_roadmap.md

---

## 📈 Valor de negocio

✔ Automatización
✔ Reducción de riesgo
✔ Trazabilidad
✔ Eficiencia

---

## 🚀 Próximos pasos

✔ APIs reales
✔ IA
✔ IoT
✔ Arquitectura distribuida

---

## 👩‍💻 Autor

Verónica Maldonado Céspedes
Cloud & DevOps Delivery Manager
Project Manager | Transformación Digital

