🔙 Volver:
- [README principal](../README.md)
  
# 🔄 Flujo Operacional — Intelligent Logistics Control Platform

## 🎯 Propósito

Definir y validar el flujo completo de decisiones operacionales del sistema, integrando validación documental, control de acceso y evaluación de riesgo, con el objetivo de asegurar operaciones logísticas seguras, controladas y trazables.

Este flujo representa el núcleo funcional del MVP, donde se orquesta la lógica de validación previa a la ejecución de una operación.

---

## 🧠 Enfoque del Modelo

La solución implementa un **motor de decisiones secuencial**, donde cada etapa evalúa una condición específica del proceso logístico.

El resultado es una **decisión consolidada**, que puede:

* Aprobar la operación
* Rechazarla
* Escalarla a revisión manual

---

## 🔁 Flujo General de Decisión

```
Input Operacional
        ↓
Validación Documental
        ↓
Control de Acceso
        ↓
Evaluación de Riesgo
        ↓
Orquestación de Decisión
        ↓
Resultado Final + Notificación
```

---

## ⚙️ Etapas del Flujo

### 1. 📄 Validación Documental

Se valida que la operación cuente con la documentación requerida:

* Documentos de importación/exportación
* Validación con ente regulador (simulado en el MVP)

**Regla:**

* Si faltan documentos → `REJECTED`

---

### 2. 🚛 Control de Acceso Operacional (Ingreso a Puerto)

Se valida la autorización de ingreso al puerto para realizar el retiro de mercancía con destino a bodega.

Este control representa un punto crítico del proceso logístico, donde se asegura que únicamente operaciones válidas y previamente autorizadas puedan acceder al recinto portuario.

Se validan las siguientes condiciones:

- Camión autorizado para retiro de carga
- Conductor habilitado y validado
- Asociación correcta entre camión, conductor y operación
- Cumplimiento de ventana horaria asignada
- Autorización de ingreso al puerto

**Regla:**

- Acceso inválido o no autorizado → `REJECTED`

---

### 3. ⚠️ Evaluación de Riesgo Logístico

Se analizan condiciones de riesgo asociadas a la operación:

* Eventos GPS (simulado)
* Manipulación de carga
* Fatiga del conductor

**Regla:**

* Riesgo alto → `REVIEW_REQUIRED`

---

### 4. 🧩 Orquestación de Decisión

Se consolidan los resultados de todas las etapas mediante reglas de negocio:

| Condición        | Resultado       |
| ---------------- | --------------- |
| Error documental | REJECTED        |
| Acceso inválido  | REJECTED        |
| Riesgo alto      | REVIEW_REQUIRED |
| Todo válido      | APPROVED        |

---

### 5. 🎟️ Resultado y Notificación

Se genera:

* Estado final de la operación
* Respuesta estructurada del sistema
* Notificación (simulada en MVP)

---

## 📊 Estados del Sistema

| Estado          | Descripción                |
| --------------- | -------------------------- |
| APPROVED        | Operación autorizada       |
| REJECTED        | Operación bloqueada        |
| REVIEW_REQUIRED | Requiere validación manual |

---

## 📌 Diagrama del Flujo Operacional

![Flujo Operacional](../diagrams/flujo_operacional_general.png)

---

## 🔗 Relación con la API

Este flujo es ejecutado a través del endpoint principal:

POST /evaluate

El endpoint procesa los datos de entrada y retorna el estado final de la operación.

---

## 📊 Relación con el Backlog

El flujo operacional fue definido a partir de las capacidades priorizadas en el backlog del producto.

Ver detalle:

- 📊 [Product Backlog](./docs/product_backlog.md)
- 🚀 [Product Roadmap](./docs/product_roadmap.md)

---

## 🧭 Contexto dentro del MVP

Este flujo corresponde al **MVP1 — Validación del Flujo Operacional**, cuyo objetivo es:

* Validar la lógica de decisiones
* Simular condiciones reales del negocio
* Preparar la base para futuras integraciones

---

## 🔮 Evolución del Flujo

Este modelo está diseñado para evolucionar hacia:

* Integración con APIs externas (aduanas, transporte)
* Incorporación de modelos de IA para scoring de riesgo
* Integración con dispositivos IoT (GPS, sensores)
* Automatización completa del proceso operativo

---

## 💡 Valor de Negocio

La implementación de este flujo permite:

* Reducir riesgos operacionales
* Estandarizar decisiones
* Mejorar la trazabilidad
* Aumentar la eficiencia en procesos logísticos

---

## 🏗️ Relación con la Arquitectura

Cada etapa del flujo operacional se encuentra implementada mediante componentes específicos de la solución:

- Validación documental → document_validator
- Control de acceso → access_control
- Evaluación de riesgo → risk_assessor
- Orquestación de decisión → orchestrator
- Exposición del servicio → API REST (FastAPI)

👉 Ver arquitectura completa:
- [Arquitectura de la solución](./arquitectura.md)
