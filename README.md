🚀 Intelligent Logistics Control Platform  

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Passed-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-90%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)

👉 API inteligente para automatizar decisiones operacionales en procesos logísticos críticos

🔗 Swagger local: http://127.0.0.1:8000/docs

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
| Documentos faltantes | REJECTED | ![Caso1](docs/rejected_documents.png) |
| Acceso inválido | REJECTED | ![Caso2](docs/rejected_access.png) |
| Riesgo alto | REVIEW_REQUIRED | ![Caso3](docs/high_risk.png) |
| Operación válida | APPROVED | ![Caso4](docs/approved.png) |

👉 Estas evidencias demuestran el comportamiento real del sistema.

---

### ❌ Caso 1: Rechazo por documentos faltantes

* Documentos requeridos ausentes
* Acceso no autorizado

👉 Resultado:

```json
"operation_status": "REJECTED"
```

---

### ❌ Caso 2: Documento expirado

* Licencia vencida
* Acceso permitido pero inválido documentalmente

👉 Resultado:

```json
"operation_status": "REJECTED"
```

---

### ⚠️ Caso 3: Riesgo alto

* Fatiga del conductor
* Zona GPS de alto riesgo
* Historial de incidentes

👉 Resultado:

```json
"operation_status": "REVIEW_REQUIRED"
```

---

### ✔️ Caso 4: Operación aprobada

* Documentación válida
* Acceso autorizado
* Riesgo bajo

👉 Resultado:

```json
"operation_status": "APPROVED"
```

---

👉 Estos escenarios demuestran la capacidad del sistema para simular decisiones operacionales en contextos logísticos reales.

### ✔️ Caso aprobado

* Documentos válidos
* Conductor autorizado
* Riesgo bajo
  👉 Resultado: **APPROVED + generación de ticket**

---

### ⚠️ Caso observado

* Documentación incompleta
* Inconsistencias en datos
  👉 Resultado: **OBSERVED + notificación**

---

### ❌ Caso rechazado

* Conductor no autorizado
* Riesgo alto (fatiga / GPS / historial)
  👉 Resultado: **REJECTED + alerta**

---

👉 Esto simula comportamiento real en sistemas logísticos críticos.

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

* Deploy en cloud (AWS / Azure / Render)
* Integración con servicios externos (APIs reales)
* Incorporación de IA para scoring de riesgo
* Evolución hacia arquitectura distribuida

---

## 👩‍💻 Autor

**Verónica Maldonado Céspedes**
Ingeniera Civil Informática

Project Manager | Cloud & DevOps Delivery

