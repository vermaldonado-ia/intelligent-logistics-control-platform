# 🚀 Intelligent Logistics Control Platform (MVP)

Simulación de una plataforma inteligente para el control logístico y validación operacional en procesos de transporte y comercio exterior.

Este proyecto modela un flujo completo de validación y toma de decisiones, integrando:

* Validación documental (con lógica de plazos y riesgo de eliminación)
* Validación de acceso (conductor + camión)
* Evaluación de eventos operacionales (GPS y fatiga)
* Consolidación del estado de la operación
* Notificación automática al teléfono del transportista

---

## 🎯 Objetivo

Diseñar un MVP que represente cómo una organización logística puede automatizar decisiones críticas en el ingreso de mercancías a un recinto portuario, reduciendo riesgos operacionales y mejorando la trazabilidad del proceso.

---

## 🧩 Problema de Negocio

En operaciones de comercio exterior existen múltiples puntos críticos:

* Validaciones documentales manuales y lentas
* Observaciones o rechazos sin control de plazos
* Riesgo de eliminación de mercancía por incumplimiento documental
* Falta de control en el acceso de camiones y conductores
* Eventos operacionales no monitoreados (GPS, fatiga)
* Ausencia de comunicación automática hacia el transportista

Este MVP simula una solución que orquesta estas validaciones y automatiza la decisión final.

---

## ⚙️ Flujo de la Solución

1. Validación documental
2. Validación de acceso (conductor + camión)
3. Evaluación de eventos operacionales
4. Consolidación del estado de la operación
5. Notificación automática al teléfono

---

## 🏗️ Arquitectura del MVP

Input JSON
↓
Validación Documental
↓
Validación de Acceso
↓
Evaluación de Eventos
↓
Orchestrator (Motor de Decisión)
↓
Resultado Final
↓
Notificación al Teléfono

---

## 🧠 Lógica de Negocio

### 📄 Validación Documental

Estados posibles:

* approved
* observed
* rejected

Además considera:

* días disponibles para regularización
* vencimiento del plazo
* acción requerida de la agencia de aduana

Reglas:

* Aprobado → habilitada
* Observado con plazo vigente → observada
* Rechazado con plazo vigente → observada
* Observado con plazo vencido → bloqueada
* Rechazado con plazo vencido → bloqueada (riesgo de eliminación de mercancía)

---

### 🚛 Validación de Acceso

Evalúa:

* autorización del conductor
* autorización del camión

Reglas:

* No autorizado → bloqueada
* Con observaciones → observada
* Todo correcto → habilitada

---

### 📡 Evaluación de Eventos

Evalúa:

* desvío GPS (none, moderate, critical)
* fatiga del conductor (low, medium, high)

Reglas:

* Riesgo alto → bloqueada
* Riesgo medio → observada
* Sin riesgo → habilitada

---

### 🧮 Resultado Consolidado

* Si existe cualquier bloqueo → bloqueada
* Si no hay bloqueo pero sí observaciones → observada
* Si todo está correcto → habilitada

---

### 📱 Notificación al Teléfono

Si la operación es:

* habilitada o observada → se genera notificación

Contenido:

* Nombre del conductor
* RUT
* Patente
* Número de embarque
* Estado final

Salida simulada en:

output/phone_notification.txt

---

## 📂 Estructura del Proyecto

app/
├── main.py
├── orchestrator.py
└── services/
├── document_validator.py
├── access_validator.py
├── event_evaluator.py
└── notification_service.py

data/
└── sample_input.json

output/
└── phone_notification.txt

docs/
└── arquitectura.png

---

## 📥 Ejemplo de Input

{
"documents": {
"status": "observed",
"days_to_deadline": 2,
"deadline_expired": false,
"customs_agency_response_required": true
},
"driver": {
"full_name": "Juan Pérez Soto",
"rut": "12.345.678-9",
"phone": "+56912345678",
"authorized": true,
"has_observation": false
},
"vehicle": {
"license_plate": "ABCD12",
"authorized": true,
"has_observation": false
},
"shipment": {
"shipment_number": "EMB-2026-00125"
},
"events": {
"gps_deviation": "moderate",
"fatigue_level": "low"
}
}

---

## 📤 Ejemplo de Resultado

{
"final_status": "observada"
}

---

## 🖼️ Diagrama de Arquitectura

Ubicación del archivo:

docs/arquitectura.png

El diagrama representa:

* flujo completo de validaciones
* motor de decisión
* generación de notificación

---

## 🚀 Ejecución

Desde la carpeta app:

python main.py

---

## 💡 Valor del Proyecto

Este MVP demuestra:

* Modelamiento de reglas de negocio complejas
* Orquestación de procesos operacionales
* Enfoque en trazabilidad y control logístico
* Automatización de decisiones
* Integración de validaciones en un flujo único

---

## 🧠 Enfoque Profesional

Este proyecto no busca ser un sistema productivo, sino demostrar:

* capacidad de diseño de soluciones
* entendimiento de procesos logísticos reales
* estructuración de lógica de negocio
* visión de automatización operacional

---

## 🔮 Evolución del MVP

* API con FastAPI
* Integración con SMS (Twilio)
* Dashboard de monitoreo
* Motor de reglas configurable
* Integración con sistemas aduaneros

---

## 👩‍💻 Autor

Proyecto desarrollado como parte de portafolio profesional en:

* Gestión de proyectos TI
* Transformación digital
* Cloud & DevOps
* Automatización de procesos

