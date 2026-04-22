# 🚀 Plataforma Inteligente de Control Logístico y Validación Operacional

> Simulación de solución tecnológica para automatizar procesos logísticos, validación documental y control de acceso en operaciones de transporte y comercio exterior.  
> Enfocado en la integración de procesos operacionales, trazabilidad y reducción de riesgos logísticos.

---

## 🎯 Objetivo

Diseñar y desarrollar un prototipo funcional que simule la automatización de decisiones en procesos logísticos, integrando:

- Control de acceso de conductores y camiones a recintos operacionales
- Validación documental en procesos de importación/exportación (simulación)
- Monitoreo de eventos de riesgo logístico (GPS y condiciones del conductor)
- Orquestación de decisiones para determinar el estado de la operación

---

## 🧩 Problema de Negocio

En operaciones logísticas y de comercio exterior existen múltiples puntos críticos que impactan la continuidad y seguridad:

- Validaciones manuales de acceso al puerto
- Falta de control en el ingreso de camiones al recinto portuario
- Ingreso de camiones no autorizados con riesgo de robo de carga
- Procesos documentales lentos y propensos a errores
- Falta de trazabilidad en eventos operacionales
- Robo de mercancía tanto en carretera como dentro del puerto
- Riesgo de fatiga de conductores durante el traslado

Adicionalmente, la operación logística está sujeta a restricciones de tiempo:

- Los camiones deben cumplir ventanas de atención en el puerto
- Si no se cumple el turno asignado, la carga puede quedar en piso
- Existen multas por retraso en la operación

Estos factores generan:

- Pérdidas económicas por robos o multas  
- Riesgos de seguridad operacional  
- Retrasos en la cadena logística  
- Baja eficiencia en la toma de decisiones  

---

## 💡 Solución Propuesta

Se propone una plataforma que automatiza la evaluación de una operación logística mediante un **motor de decisiones**, integrando distintas fuentes de validación:

### Capacidades principales

- ✅ Control de acceso portuario (conductor y camión)
- ✅ Validación documental (simulación de procesos regulatorios)
- ✅ Monitoreo de riesgo logístico (GPS – robo o desvío de carga)
- ✅ Monitoreo de condiciones del conductor (fatiga)
- ✅ Evaluación de cumplimiento de ventanas operacionales
- ✅ Orquestación de resultados en una decisión consolidada

---

## ⚙️ Flujo de la Operación

1. Se recibe una solicitud de operación logística
2. El camión se presenta en el punto de control (simulación de tótem)
3. Se valida el acceso del conductor y camión
4. Se evalúa la documentación de la carga
5. Se analizan eventos operacionales:
   - Alerta GPS (posible robo o desvío)
   - Fatiga del conductor
6. Se valida cumplimiento de ventana horaria
7. Se ejecuta el motor de decisiones
8. Se entrega un resultado consolidado

---

## 🧠 Lógica de Decisión

### Resultado por módulo

- Acceso: `APROBADO | OBSERVADO | RECHAZADO`
- Documentación: `APROBADO | OBSERVADO | RECHAZADO`
- GPS: `NORMAL | ALERTA`
- Fatiga: `NORMAL | ALERTA`

---

### Resultado consolidado

| Condición | Resultado |
|----------|--------|
| Todo aprobado y sin alertas | ✅ Operación habilitada |
| Existen alertas o desviaciones | ⚠️ Operación con observaciones |
| Acceso o documentación rechazada | ❌ Operación bloqueada |

---

## 🔄 Flujo General del Proceso

![Flujo Operacional](./diagrams/flujo_operacional_general.png)

---

## 🧪 Ejemplo de Input

```json
{
  "conductor_autorizado": true,
  "camion_autorizado": true,
  "ventana_horaria_valida": true,
  "documentos_completos": true,
  "datos_consistentes": true,
  "gps_alerta": false,
  "fatiga_detectada": false
}
