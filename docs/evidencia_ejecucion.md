# 📸 Evidencia de Ejecución — Intelligent Logistics Control Platform

## 🎯 Propósito

Demostrar la ejecución real del flujo operacional mediante casos de prueba representativos, evidenciando el comportamiento del sistema ante distintos escenarios logísticos.

---

## 🧠 Enfoque

Se simulan operaciones logísticas con diferentes condiciones de entrada para validar:

* Reglas de negocio
* Flujo de decisiones
* Estados finales del sistema

Cada caso representa una situación real del proceso operativo.

---

## 🧪 Casos de prueba ejecutados

| Caso   | Escenario                      | Resultado esperado   | Estado          |
| ------ | ------------------------------ | -------------------- | --------------- |
| Caso 1 | Documentación incompleta       | Rechazo de operación | REJECTED        |
| Caso 2 | Acceso no autorizado al puerto | Rechazo de operación | REJECTED        |
| Caso 3 | Riesgo operacional alto        | Revisión manual      | REVIEW_REQUIRED |
| Caso 4 | Operación válida               | Aprobación           | APPROVED        |

---

## 📊 Resultados del sistema

### 🔴 Caso 1 — Documentos faltantes

La operación es rechazada debido a la ausencia de documentación obligatoria.

📌 Evidencia:

![Caso 1](../diagrams/reject_documents.png)

---

### 🔴 Caso 2 — Acceso inválido al puerto

Se detecta que el camión o conductor no está autorizado para el retiro de mercancía.

📌 Evidencia:

![Caso 2](../diagrams/reject_access.png)

---

### 🟡 Caso 3 — Riesgo alto

Se identifican condiciones de riesgo que requieren revisión manual antes de continuar.

📌 Evidencia:

![Caso 3](../diagrams/high_risk.png)

---

### 🟢 Caso 4 — Operación aprobada

La operación cumple todas las validaciones y es autorizada.

📌 Evidencia:

![Caso 4](../diagrams/approved.png)

---

## 🔗 Relación con el flujo operacional

Los resultados observados corresponden directamente a las reglas definidas en el flujo del sistema.

👉 Ver flujo:

* [Flujo Operacional](./flujo_operacional.md)

---

## 🔗 Relación con la arquitectura

La ejecución de estos casos es soportada por los componentes definidos en la solución.

👉 Ver arquitectura:

* [Arquitectura de la solución](./arquitectura.md)

---

## 💡 Valor de esta evidencia

Esta sección permite validar que:

* El flujo operacional está correctamente implementado
* Las reglas de negocio se ejecutan como se espera
* El sistema responde de forma consistente ante distintos escenarios

---

## 🧭 Conclusión

La solución no solo define un flujo teórico, sino que demuestra su ejecución mediante casos concretos, permitiendo validar su comportamiento en un entorno controlado.

---

## 🔙 Navegación

* [Volver al README](../README.md)
* [Ver Flujo Operacional](./flujo_operacional.md)
* [Ver Arquitectura](./arquitectura.md)
