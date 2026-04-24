# 🚀 Intelligent Logistics Control Platform

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=vermaldonado-ia_intelligent-logistics-control-platform\&metric=alert_status)
![Coverage](https://sonarcloud.io/api/project_badges/measure?project=vermaldonado-ia_intelligent-logistics-control-platform\&metric=coverage)

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

## 🏗️ Arquitectura

```bash
app/
├── api.py                # API FastAPI
├── orchestrator.py       # Orquestador de decisiones
└── services/             # Lógica de negocio desacoplada
    ├── document_validator.py
    ├── access_control.py
    ├── risk_assessor.py
    ├── ticket_generator.py
    └── notification_service.py

tests/                    # Pruebas automatizadas
sample_data/              # Datos de prueba
diagrams/                 # Diagramas de flujo
```

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

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Enfoque Arquitectónico

Este proyecto demuestra:

* Diseño de soluciones orientadas a negocio
* Orquestación de lógica compleja
* Separación de responsabilidades (services layer)
* Testing automatizado
* Integración CI/CD
* Control de calidad continuo

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

