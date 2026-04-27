🚀 Intelligent Logistics Control Platform  

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Passed-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-90%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)

👉 Plataforma desplegada en producción que simula decisiones operacionales en procesos logísticos críticos, integrando validación documental, control de acceso y análisis de riesgo en tiempo real.

🔗 API en producción: https://intelligent-logistics-control-platform.onrender.com

🔗 Swagger: https://intelligent-logistics-control-platform.onrender.com/docs

✔ Deploy automático desde GitHub  
✔ API pública accesible  
✔ Documentación interactiva  
✔ Runtime en cloud

⚠️ Nota: al estar en free tier, puede tardar unos segundos en iniciar.

## 📸 Evidencia de despliegue en producción

## 📸 Evidencia real en producción

### 🌐 API desplegada en Render
![Render](diagrans/render_deploy.png)

### 📘 Swagger en producción
![Swagger](diagrams/swagger.png)

### ⚙️ Logs de ejecución
![Logs](diagrams/logs.png)

---

## 🧠 Descripción

Simulación de una **plataforma inteligente de control logístico**, diseñada para automatizar decisiones críticas en procesos de transporte y comercio exterior.

El sistema integra validación documental, control de acceso y análisis de riesgo operacional, permitiendo simular un flujo real de decisión automatizada en entornos logísticos complejos.

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

| Antes | Después |
|------|--------|
| Validaciones manuales | Validación automatizada |
| Procesos lentos | Decisiones en tiempo real |
| Alto riesgo operativo | Evaluación automatizada de riesgo |
| Baja trazabilidad | Trazabilidad completa de decisiones |

---

## 💡 Solución

Se desarrolló una API que simula un **motor de decisiones inteligente**, capaz de:

✔️ Validar documentación
✔️ Evaluar condiciones de acceso
✔️ Analizar riesgo operacional
✔️ Orquestar decisiones
✔️ Generar tickets de acceso
✔️ Emitir notificaciones

---

## 🏗️ Arquitectura de la solución

La solución está diseñada bajo un enfoque modular, separando responsabilidades en capas:

* **API Layer** → exposición de endpoints (FastAPI)
* **Orchestration Layer** → lógica de decisión central
* **Services Layer** → reglas de negocio desacopladas

### Componentes principales

```bash
app/
├── api.py                # API FastAPI
├── orchestrator.py       # Motor de decisiones
└── services/             # Lógica de negocio
```

👉 Este diseño permite:

* Escalabilidad
* Mantenibilidad
* Separación de responsabilidades
* Evolución hacia microservicios

---

🧠 Enfoque del Proyecto

Este proyecto está diseñado desde una perspectiva de Delivery y negocio, no solo técnica.

Se enfoca en:

✔ Modelamiento de decisiones operacionales reales  
✔ Orquestación de múltiples reglas de negocio  
✔ Simulación de escenarios críticos de riesgo  
✔ Generación de outputs trazables y explicables  

👉 Representa cómo un sistema real tomaría decisiones en entornos logísticos complejos.

---

## 🔄 Flujo de la Solución

1. Recepción de datos de operación logística
2. Validación de documentos
3. Evaluación de acceso (conductor, vehículo, carga)
4. Análisis de riesgo (fatiga, GPS, historial)
5. Toma de decisión automatizada
6. Generación de ticket
7. Envío de notificación

📌 Ver diagrama:
`diagrams/flujo_operacional_general.png`

---

🚨 Escenarios de decisión (evidencia real)

La API fue validada mediante pruebas reales en Swagger, simulando distintos escenarios operacionales:

❌ Caso 1: Rechazo por documentos faltantes  
👉 Resultado: "operation_status": "REJECTED"

❌ Caso 2: Documento expirado  
👉 Resultado: "operation_status": "REJECTED"

⚠️ Caso 3: Riesgo alto  
👉 Resultado: "operation_status": "REVIEW_REQUIRED"

✔️ Caso 4: Operación aprobada  
👉 Resultado: "operation_status": "APPROVED"

---

### 📸 Evidencia de ejecución (Swagger)

| Caso | Resultado | Evidencia |
|------|----------|----------|
| Documentos faltantes | REJECTED | ![Caso1](diagrams/rejected_documents.png) |
| Acceso inválido | REJECTED | ![Caso2](diagrams/rejected_access.png) |
| Riesgo alto | REVIEW_REQUIRED | ![Caso3](diagrams/high_risk.png) |
| Operación válida | APPROVED | ![Caso4](diagrams/approved.png) |

👉 Estos escenarios demuestran la capacidad del sistema para simular decisiones operacionales en contextos logísticos reales.

---

## 🔌 Endpoints

### ✔️ Health Check

```
GET /health
```

Respuesta:

```json
{"status": "ok"}
```

---

### ✔️ Evaluación de Operación

```
POST /evaluate
```

Ejemplo:

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
    },
    "port_access_allowed": true,
    "gps": {
      "zone": "warning"
    },
    "incident_history": {
      "previous_incidents": 1
    },
    "documents": {
      "driver_license": {
        "present": true,
        "expiry_date": "2027-12-31"
      },
      "vehicle_permit": {
        "present": true,
        "expiry_date": "2027-10-15"
      },
      "cargo_manifest": {
        "present": true,
        "expiry_date": "2027-08-01"
      }
    }
  }
}
```

---

## 🧪 Pruebas y Calidad

Ejecución de tests:

```bash
pytest -v
```

Cobertura:

```bash
pytest --cov=app
```

✔️ Integrado en CI con GitHub Actions
✔️ Validación de calidad con SonarCloud
✔️ Control de cobertura automatizado

---

## ⚙️ Tecnologías

* Python
* FastAPI
* Pytest
* Flake8
* Coverage
* GitHub Actions (CI)
* SonarCloud (Quality Gate)

---

## ⚙️ Integración CI/CD y Calidad

Este proyecto incorpora un pipeline automatizado de integración continua (CI) utilizando GitHub Actions.

### ✔️ Validaciones automáticas

* Ejecución de tests con Pytest
* Análisis de código con Flake8
* Formateo con Black
* Generación de cobertura de código
* Análisis de calidad con SonarCloud

### 🔄 Flujo del pipeline

```text
Push → GitHub Actions → Tests → Lint → Coverage → SonarCloud → Resultado
```

👉 Esto permite asegurar calidad desde etapas tempranas del desarrollo.

---

## 📊 Evidencia del pipeline

El proyecto cuenta con ejecución real de pipeline CI y análisis de calidad:

* ✔️ CI Pipeline ejecutándose en cada commit
* ✔️ Quality Gate validado con SonarCloud
* ✔️ Cobertura de código integrada

👉 Ver en pestaña **Actions** del repositorio.

---

## 🚀 Ejecución local

```bash
pip install -r requirements.txt
python -m uvicorn app.api:app --reload
```

Acceder a:

🔗 Swagger local (ejecución en entorno de desarrollo):
http://127.0.0.1:8000/docs

---

## 📈 Valor para el negocio

Esta solución simula un escenario real donde:

* Se reduce el riesgo de acceso no autorizado
* Se mejora la toma de decisiones operacionales
* Se automatiza la validación documental
* Se incrementa la trazabilidad del proceso

👉 Base directa para sistemas de:

* Control portuario
* Transporte terrestre
* Aduanas / comercio exterior
* Plataformas logísticas inteligentes

✔ Reducción de exposición a riesgos operacionales  
✔ Mejora en tiempos de validación y toma de decisiones  
✔ Incremento en trazabilidad y control operacional  
✔ Base para automatización de procesos logísticos críticos  

---

## 🚀 Próximos pasos

Este proyecto puede evolucionar hacia una solución más robusta incorporando:

✔ Integración con APIs reales de validación documental, transporte o comercio exterior  
✔ Modelos de IA para scoring predictivo de riesgo operacional  
✔ Arquitectura distribuida basada en microservicios  
✔ Integración con datos IoT/GPS para monitoreo de ruta, fatiga y alertas operacionales  

> Estos puntos representan una evolución futura del MVP y no forman parte del alcance actual implementado.

---

## 🎯 Valor diferencial del proyecto

Este proyecto no solo demuestra habilidades técnicas, sino capacidad de:

✔ Diseñar soluciones orientadas a negocio  
✔ Modelar procesos operacionales reales  
✔ Implementar automatización de decisiones  
✔ Integrar prácticas DevOps (CI/CD + despliegue)  
✔ Entregar soluciones desplegadas en producción  

👉 Representa el rol de un Delivery Manager en entornos tecnológicos modernos.

---

## 👩‍💻 Autor

**Verónica Maldonado Céspedes**
Ingeniera Civil Informática

Project Manager | Cloud & DevOps Delivery

