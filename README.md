# 🚀 Intelligent Logistics Control Platform (MVP)

Simulación de una plataforma inteligente para el control logístico y validación operacional en procesos de transporte y comercio exterior.

Este MVP modela un flujo realista desde la validación documental previa por el ente fiscalizador hasta el monitoreo de la carga en tránsito, integrando control operativo, gestión de riesgos y automatización de decisiones.

---

## 🎯 Objetivo

Automatizar la validación documental previa por parte del ente fiscalizador (aduana), el control de ingreso al puerto, la salida de mercancía y el monitoreo del transporte, reduciendo riesgos operacionales y asegurando trazabilidad completa del proceso logístico.

---

## 🧩 Problema de Negocio

En operaciones reales de comercio exterior:

* La documentación se valida manualmente o fuera de tiempo
* Existen observaciones o rechazos sin control efectivo de plazos
* Hay errores en los datos de ingreso al puerto (conductor, camión, embarque)
* No existe control robusto sobre eventos críticos durante el transporte
* No hay comunicación automática clara hacia el transportista

Esto genera:

* retrasos operacionales
* riesgo de fraude o robo de mercancía
* errores en la ejecución logística
* riesgo de eliminación de mercancía por incumplimiento documental

---

## ⚙️ Flujo de la Solución

1. Validación documental (ente fiscalizador)
2. Validación de acceso al puerto
3. Notificación al teléfono (habilita ingreso)
4. Salida del camión del puerto hacia destino
5. Monitoreo de eventos operacionales (en tránsito)
6. Motor de decisión
7. Resultado final de la operación

---

## 🏗️ Arquitectura del MVP

Validación Documental
↓
Validación de Acceso
↓
Notificación al Teléfono (habilita tranca de acceso)
↓
Salida del Puerto (inicio de tránsito)
↓
Monitoreo de Eventos
↓
Motor de Decisión
↓
Resultado Final

---

## 🧠 Lógica de Negocio

---

### 📄 1. Validación Documental (PREVIA AL ARRIBO)

Se valida antes de que la carga llegue al puerto.

#### Documentos evaluados:

* Facturas comerciales
* Órdenes de compra
* Datos de la carga
* Datos del importador/exportador
* Documentos de transporte
* Seguros
* Certificados y permisos regulatorios

#### Estados:

* Aprobada → habilitada
* Observada con plazo → observada
* Rechazada con plazo → observada
* Observada sin regularizar → bloqueada
* Rechazada sin regularizar → bloqueada

⚠️ Riesgo crítico:
Si no se regulariza dentro del plazo → posible eliminación de mercancía

---

### 🚛 2. Validación de Acceso al Puerto

Evalúa si el camión puede ingresar.

#### Datos evaluados:

* Fecha y hora de ingreso
* Conductor (nombre, RUT, teléfono)
* Camión (patente)
* Número de embarque
* Puerta de carga asignada

#### Reglas:

* ❌ Datos inválidos → No entra al puerto
* ⚠️ Datos incompletos → Queda en espera de validación por agencia de aduana
* ✅ Datos completos y validados → Acceso autorizado

---

### 📱 3. Notificación al Teléfono (AUTORIZACIÓN DE INGRESO)

Se ejecuta inmediatamente después de validar el acceso.

#### Información enviada:

* Nombre del conductor
* RUT
* Patente del camión
* Número de embarque
* Puerta de carga asignada
* Fecha y hora de ingreso

#### Impacto operativo:

* Habilita la apertura automática de la tranca de acceso
* Permite el ingreso físico del camión al puerto

---

### 🧾 Ticket Digital de Acceso

Como complemento operativo, el sistema genera un ticket digital con:

* Fecha y hora de emisión
* Código único de ticket
* Estado de acceso
* Observaciones
* Código QR simulado

Este ticket actúa como evidencia del proceso y trazabilidad de la operación.

---

### 🚚 4. Salida del Camión del Puerto

Una vez cargada la mercancía:

* Se autoriza salida del puerto
* Se inicia el tránsito hacia la bodega destino

Este punto marca el inicio del monitoreo real.

---

### 📡 5. Monitoreo de Eventos (EN TRÁNSITO)

Este proceso ocurre únicamente cuando la carga ya está en el camión.

#### Eventos evaluados:

* Desvío de ruta (GPS)
* Manipulación o violación de candado GPS
* Robo o intento de asalto
* Fatiga del conductor

#### Niveles de riesgo:

* 🔴 Alto → Bloqueada
* 🟡 Medio → Observada
* 🟢 Bajo → Habilitada

---

### 🧠 6. Motor de Decisión

Consolida toda la información operacional.

#### Reglas:

* 🔴 Evento crítico (asalto o manipulación GPS)
  → Genera alarma automática a la comisaría más cercana

* 🟡 Fatiga del conductor
  → Activa alarma en cabina
  → Obliga detención para cambio de conductor

* 🟢 Sin riesgo
  → Operación continúa normalmente

---

### 📊 7. Resultado Final

Estados posibles:

* ✅ HABILITADA → operación segura
* ⚠️ OBSERVADA → requiere acción
* ❌ BLOQUEADA → operación detenida

---

## 📂 Estructura del Proyecto

app/
├── main.py
├── orchestrator.py
└── services/
├── document_validator.py
├── access_validator.py
├── event_evaluator.py
├── notification_service.py
└── ticket_generator.py

data/
└── sample_input.json

output/
├── phone_notification.txt
└── access_ticket.txt

docs/
└── arquitectura.png

---

## 🖼️ Diagrama de Arquitectura

El siguiente diagrama representa el flujo completo del sistema:

![Diagrama de Arquitectura](diagrams/flujo_operacional_general.png)

---

## 🚀 Ejecución

```bash
python main.py
```

---

## 📥 Input del Sistema

Simula:

* Validación documental
* Datos de acceso
* Conductor y vehículo
* Embarque
* Eventos operacionales

---

## 📤 Output del Sistema

* Estado final de la operación
* Notificación al teléfono
* Ticket digital de acceso
* Evidencia del proceso

---

## 💡 Valor del Proyecto

Este MVP demuestra:

* Modelamiento de procesos logísticos reales
* Control de acceso portuario
* Gestión de riesgo en transporte
* Automatización de decisiones
* Integración entre negocio y tecnología

---

## 🧠 Enfoque Profesional

Este proyecto refleja:

* Diseño de arquitectura de solución
* Pensamiento orientado a procesos
* Traducción de reglas de negocio a lógica técnica
* Enfoque en eficiencia operativa y reducción de riesgos

---

## 🔮 Evolución

* Integración con GPS real
* Integración con sistemas de seguridad pública
* API REST con FastAPI
* Dashboard en tiempo real
* Motor de reglas configurable

---

## 👩‍💻 Autor

Proyecto desarrollado como parte de portafolio profesional en:

* Delivery Management
* Transformación Digital
* Cloud & DevOps
* Automatización de procesos
