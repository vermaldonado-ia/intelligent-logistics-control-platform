# 🚀 Intelligent Logistics Control Platform

Simulación de una plataforma inteligente para el **control de acceso logístico, validación documental y evaluación de riesgo operacional** en procesos de transporte y comercio exterior.

---

## 🎯 Objetivo

Diseñar una solución tecnológica que permita **automatizar decisiones operacionales críticas**, reduciendo riesgos, errores manuales y tiempos de validación en entornos logísticos.

---

## 🧩 Problema de Negocio

En operaciones logísticas reales existen múltiples puntos críticos:

* Validación manual de documentos
* Ingreso de camiones no autorizados
* Falta de control sobre conductores y vehículos
* Evaluación tardía de riesgos operacionales
* Procesos lentos y propensos a error

👉 Esto impacta directamente en:

* Seguridad
* Continuidad operacional
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
├── orchestrator.py      # Orquestador principal
└── services/            # Lógica de negocio
    ├── document_validator.py
    ├── access_control.py
    ├── risk_assessor.py
    ├── ticket_generator.py
    └── notification_service.py

tests/                   # Pruebas automatizadas
sample_data/             # Datos de prueba
diagrams/                # Diagramas de flujo
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

📌 Ver diagrama en:

```
diagrams/flujo_operacional_general.png
```

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

Ejemplo de request:

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

## 🧪 Pruebas

Ejecución de tests:

```bash
pytest -v
```

Cobertura:

```bash
pytest --cov=app
```

---

## ⚙️ Tecnologías

* Python
* FastAPI
* Pytest
* Flake8
* Coverage

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

## 🧠 Enfoque

Este proyecto no busca solo implementar código, sino demostrar:

* Diseño de soluciones orientadas a negocio
* Orquestación de lógica compleja
* Separación de capas
* Buenas prácticas de desarrollo
* Base para integración CI/CD y calidad

---

## 📌 Próximos pasos

* Integración CI/CD (GitHub Actions)
* Quality Gate con SonarCloud
* Deploy en cloud (Azure / Render)
* Evolución hacia arquitectura distribuida

---

## 👩‍💻 Autor

Verónica Maldonado Céspedes
Ingeniera Civil Informática
Project Manager | Cloud & DevOps Delivery

---

