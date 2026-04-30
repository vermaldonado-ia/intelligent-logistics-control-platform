# ⚙️ DevOps y CI/CD — Intelligent Logistics Control Platform

## 🎯 Propósito

Describir cómo se automatiza la validación, integración y despliegue de la solución mediante prácticas de integración continua (CI) y despliegue continuo (CD).

---

## 🧠 Enfoque

La solución incorpora un pipeline de CI/CD que permite:

* Validar automáticamente los cambios en el código
* Asegurar calidad mínima antes de integrar
* Estandarizar el proceso de entrega

Este enfoque permite reducir errores y mejorar la confiabilidad del sistema.

---

## 🔄 Flujo CI/CD

```id="r4b1hz"
Desarrollador → Pull Request → CI Pipeline → Validaciones → Merge → Deploy
```

---

## 🔧 Integración Continua (CI)

La integración continua se implementa mediante **GitHub Actions**.

Cada vez que se realiza un cambio en el repositorio:

1. Se ejecutan pruebas automatizadas
2. Se valida calidad del código
3. Se verifica cobertura de pruebas

---

### 🧪 Validaciones realizadas

* ✔ Ejecución de tests (`pytest`)
* ✔ Cobertura de código (`pytest-cov`)
* ✔ Análisis de calidad (`flake8`)
* ✔ Formato de código (`black`)

Estas validaciones permiten detectar errores antes de integrar cambios.

---

## 🚀 Despliegue Continuo (CD)

La solución puede ser desplegada en un entorno cloud (por ejemplo, Render o AWS), permitiendo exponer la API para pruebas reales.

Esto permite:

* Validar comportamiento en entorno real
* Simular uso del sistema
* Exponer documentación (Swagger)

---

## 🌐 API en ejecución

El sistema expone:

* Endpoint principal: `POST /evaluate`
* Documentación interactiva (Swagger)

Esto permite probar el flujo completo de forma directa.

---

## 📊 Evidencia del Pipeline

El pipeline valida automáticamente cada cambio realizado.

📌 Ejemplo de validaciones:

* Ejecución exitosa de tests
* Validación de cobertura
* Análisis de calidad sin errores críticos

*(Aquí puedes agregar capturas del pipeline si las tienes)*

---

## 🔗 Relación con la solución

El pipeline CI/CD asegura que:

* La lógica del flujo operacional se mantenga consistente
* Las validaciones sigan funcionando correctamente
* La solución pueda evolucionar sin romper funcionalidades

👉 Ver flujo:

* [Flujo Operacional](./flujo_operacional.md)

---

## 🔗 Relación con calidad de código

La calidad del código es validada mediante herramientas automáticas.

👉 Ver detalle:

* [Evidencia SonarCloud](./evidencia_sonarcloud.md)

---

## 💡 Valor de negocio

La incorporación de CI/CD permite:

* Reducir errores en producción
* Aumentar la velocidad de entrega
* Mejorar la calidad del software
* Estandarizar procesos de desarrollo

---

## 🧭 Contexto

Este enfoque refleja la adopción de prácticas modernas de desarrollo, alineadas con entornos de trabajo colaborativos y ágiles.

---

## 🔙 Navegación

* [Volver al README](../README.md)
* [Ver Flujo Operacional](./flujo_operacional.md)
* [Ver Arquitectura](./arquitectura.md)
* [Ver Evidencia de Ejecución](./evidencia_ejecucion.md)
