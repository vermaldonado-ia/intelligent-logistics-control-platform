# 🚀 Intelligent Logistics Control Platform (MVP)

Simulación de una plataforma inteligente para el control logístico y validación operacional en procesos de transporte y comercio exterior.

Este MVP modela un flujo realista desde la validación documental previa hasta el monitoreo de la carga en tránsito, integrando control operativo, gestión de riesgos y automatización de decisiones.

---

## 🎯 Objetivo

Automatizar el control de ingreso al puerto, salida de mercancía y monitoreo del transporte, reduciendo riesgos operacionales y asegurando trazabilidad completa del proceso logístico.

---

## 🧩 Problema de Negocio

En operaciones reales de comercio exterior:

* La documentación se valida tarde o manualmente
* Los accesos al puerto no están completamente controlados
* Existen errores en datos de ingreso (conductor, camión, embarque)
* No hay control sobre eventos críticos durante el transporte
* No existe comunicación automática clara hacia el transportista

Esto genera:

* retrasos
* riesgos de fraude o robo
* errores operacionales
* riesgo de eliminación de mercancía

---

## ⚙️ Flujo de la Solución (ACTUALIZADO)

1. Validación documental
2. Validación de acceso al puerto
3. Notificación al teléfono (autorización de ingreso)
   2.5 Salida del camión del puerto hacia destino
4. Monitoreo de eventos operacionales durante el trayecto
5. Motor de decisión
6. Resultado final de la operación

---

## 🏗️ Arquitectura del MVP

Validación Documental
↓
Validación de Acceso
↓
Notificación al Teléfono (habilita ingreso)
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
* Datos de la carga (peso, bultos, origen, destino)
* Datos del importador
* Documentos de transporte
* Seguros
* Certificados y permisos

#### Estados:

* Aprobada → habilitada
* Observada con plazo → observada
* Rechazada con plazo → observada
* Observada sin regularizar → bloqueada
* Rechazada sin regularizar → bloqueada

⚠️ Riesgo crítico:

> Si no se regulariza dentro del plazo → posible eliminación de mercancía

---

### 🚛 2. Validación de Acceso al Puerto

Evalúa si el camión puede ingresar.

#### Datos evaluados:

* Fecha y hora de ingreso
* Conductor (nombre, RUT, teléfono)
* Camión (patente)
* Número de embarque
* Cita o reserva

#### Reglas:

* ❌ Datos inválidos → NO entra al puerto
* ⚠️ Datos incompletos → queda en espera de validación por agencia de aduana
* ✅ Datos completos y válidos → entra al puerto

---

### 📱 6. Notificación al Teléfono (AUTORIZACIÓN DE INGRESO)

Se ejecuta inmediatamente después del acceso validado.

#### Información enviada:

* Nombre del conductor
* RUT
* Patente del camión
* Número de embarque
* **Número de puerta de carga asignada**
* Fecha y hora de ingreso

#### Impacto operativo:

* Levanta automáticamente la tranca de acceso
* Permite el ingreso del camión al puerto

---

### 🚚 2.5 Salida del Camión del Puerto

Una vez cargada la mercancía:

* Se autoriza salida del puerto
* Se inicia el tránsito hacia la bodega destino

Este punto marca el inicio del monitoreo real.

---

### 📡 3. Monitoreo de Eventos (EN TRÁNSITO)

⚠️ Importante:
Este proceso ocurre **solo cuando la carga ya está en el camión**

#### Eventos evaluados:

* Desvío de ruta (GPS)
* Violación de candado GPS
* Robo o intento de asalto
* Fatiga del conductor

#### Niveles de riesgo:

* 🔴 Alto → Bloqueada
* 🟡 Medio → Observada
* 🟢 Bajo → Habilitada

---

### 🧠 4. Motor de Decisión

Consolida toda la información.

#### Reglas reales:

* 🔴 Si hay evento crítico (asalto, manipulación GPS):
  → Se genera alarma automática a la comisaría más cercana

* 🟡 Si hay fatiga del conductor:
  → Se activa alarma en cabina
  → Obligación de detenerse para cambio de conductor

* 🟢 Si todo está correcto:
  → Operación continúa normalmente

---

### 📊 5. Resultado Final

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
└── notification_service.py

data/
└── sample_input.json

output/
└── phone_notification.txt

docs/
└── arquitectura.png

---

## 📥 Input del Sistema

Simula toda la operación:

* Documentación
* Conductor
* Vehículo
* Embarque
* Eventos

---

## 📤 Output del Sistema

* Estado final de la operación
* Notificación al teléfono
* Evidencia del proceso

---

## 🖼️ Diagrama

Ver:

![Diagrama de Arquitectura](docs/flujo_operacional_general.png)

---

## 🚀 Ejecución

```bash
python main.py
```

---

## 💡 Valor del Proyecto

Este MVP demuestra:

* Modelamiento de procesos logísticos reales
* Control de acceso portuario
* Gestión de riesgo en transporte
* Automatización de decisiones
* Integración de negocio + tecnología

---

## 🧠 Enfoque Profesional

Este proyecto representa:

* pensamiento de arquitectura
* diseño de flujo operacional
* entendimiento de logística real
* enfoque en automatización

---

## 🔮 Evolución

* Integración con GPS real
* Integración con Carabineros / seguridad
* API REST (FastAPI)
* Dashboard en tiempo real
* Motor de reglas configurable

---

## 👩‍💻 Autor

Proyecto orientado a portafolio profesional en:

* Delivery Management
* Transformación Digital
* Cloud & DevOps
* Automatización de procesos

