# 🚀 Plataforma Inteligente de Control Logístico y Validación Operacional

> Simulación de solución tecnológica para automatizar procesos logísticos, validación documental y control de acceso en operaciones de transporte y comercio exterior.  
> Enfocado en la integración de procesos operacionales, trazabilidad y reducción de riesgos logísticos.

---

## 🎯 Objetivo

Diseñar y desarrollar un prototipo funcional que simule la automatización de decisiones en procesos logísticos, integrando:

- Validación documental en procesos de importación/exportación (simulación)
- Control de acceso de conductores y camiones a recintos operacionales
- Monitoreo de eventos de riesgo logístico (GPS y condiciones del conductor)
- Orquestación de decisiones para determinar el estado de la operación

---

## 🧩 Problema de Negocio

En operaciones logísticas y de comercio exterior existen múltiples puntos críticos que impactan la continuidad y seguridad:

### 🔐 Seguridad
- Ingreso de camiones no autorizados al recinto portuario  
- Robo de mercancía en carretera y dentro del puerto  
- Falta de control en accesos físicos  

### ⚙️ Operación
- Procesos manuales de validación  
- Falta de trazabilidad en eventos operacionales  
- Sistemas no integrados  

### ⏱️ Cumplimiento
- Ventanas horarias estrictas en el puerto  
- Multas por retraso en la atención  
- Riesgo de que la carga quede en piso por incumplimiento de turno  

Estos factores generan:

- Pérdidas económicas por robos o multas  
- Riesgos de seguridad operacional  
- Retrasos en la cadena logística  
- Baja eficiencia en la toma de decisiones  

---

## 💡 Solución Propuesta

Se propone una plataforma que automatiza la evaluación de una operación logística mediante un **motor de decisiones**, integrando distintas fuentes de validación:

### Capacidades principales

- ✅ Validación documental (simulación basada en criterios de entidades fiscalizadoras)  
- ✅ Control de acceso portuario (conductor y camión)  
- ✅ Monitoreo de riesgo logístico (GPS – robo o desvío de carga)  
- ✅ Monitoreo de condiciones del conductor (fatiga)  
- ✅ Evaluación de cumplimiento de ventanas operacionales  
- ✅ Orquestación de resultados en una decisión consolidada  

---

## 🔄 Flujo General del Proceso

![Flujo Operacional](./diagrams/flujo_operacional_general.png)

> La validación documental considera criterios generales de cumplimiento regulatorio definidos por entidades fiscalizadoras del ámbito de comercio exterior.

---

## ⚙️ Flujo de la Operación

1. Se recibe una solicitud de operación logística  
2. Se realiza la validación documental de la carga  
3. Si la documentación es conforme, el camión se presenta en el punto de control  
4. Se valida el acceso del conductor y del camión  
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

## 🧪 Ejemplo de Input (simplificado)

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
