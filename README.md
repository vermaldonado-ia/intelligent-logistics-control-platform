# 🚀 Intelligent Logistics Control Platform

Plataforma que automatiza decisiones operacionales en procesos logísticos, integrando validación documental, control de acceso a puerto y evaluación de riesgo.

![CI](https://github.com/vermaldonado-ia/intelligent-logistics-control-platform/actions/workflows/ci.yml/badge.svg)
![Quality Gate](https://img.shields.io/badge/Quality%20Gate-Passed-brightgreen)
![Coverage](https://img.shields.io/badge/Coverage-85%25-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)

---

## 🌐 API en Producción

🔗 **API pública**
https://intelligent-logistics-control-platform.onrender.com

📘 **Swagger (documentación interactiva)**
https://intelligent-logistics-control-platform.onrender.com/docs

⚠️ Nota: al estar desplegada en free tier, la API puede tardar algunos segundos en iniciar.

---

## 🎯 Problema

En procesos logísticos, decisiones críticas como:

* Validación documental
* Acceso a puerto para retiro de mercancía
* Evaluación de riesgo

dependen de procesos manuales, generando:

* Riesgos operacionales
* Errores humanos
* Falta de trazabilidad

---

## 💡 Solución

Se implementa un motor de decisiones que automatiza la validación de operaciones antes de su ejecución, permitiendo:

* Estandarizar decisiones
* Reducir riesgos
* Mejorar control operativo

---

## 🔄 Flujo Operacional

📌 Diagrama del flujo:

![Flujo Operacional](./diagrams/flujo_operacional_general.png)

🔍 Detalle completo:

👉 [Ver flujo operacional](./docs/flujo_operacional.md)

---

## 🏗️ Arquitectura

Solución implementada como una API simple con componentes separados para validación y orquestación.

👉 [Ver arquitectura](./docs/arquitectura.md)

---

## 📸 Evidencia de Ejecución

Resultados del sistema en distintos escenarios reales:

* Documentación incompleta
* Acceso inválido al puerto
* Riesgo alto
* Operación válida

👉 [Ver evidencia completa](./docs/evidencia_ejecucion.md)

---

## ⚙️ DevOps y CI/CD

Pipeline automatizado que valida código, pruebas y calidad en cada cambio.

👉 [Ver detalle CI/CD](./docs/devops_ci_cd.md)

---

## 🧪 Calidad de Código

Evaluación mediante análisis automático con SonarCloud.

👉 [Ver evidencia](./docs/evidencia_sonarcloud.md)

---

## 📊 Gestión del Producto

El desarrollo fue gestionado bajo un enfoque de producto:

* Priorización por valor
* Trazabilidad end-to-end
* Gestión en Azure DevOps

📄 Artefactos:

* 👉 [Product Backlog](./docs/product_backlog.md)
* 👉 [Product Roadmap](./docs/product_roadmap.md)
* 👉 [Evidencia Azure DevOps](./azure_devops/boards_evidencia.md)

---

## 🚀 Ejecución local

pip install -r requirements.txt
python -m uvicorn app.api:app --reload

Swagger:
http://127.0.0.1:8000/docs

---

## 💡 Enfoque

Este proyecto refleja:

* Automatización de decisiones operacionales
* Diseño de soluciones simples orientadas a negocio
* Integración de prácticas DevOps

No utiliza inteligencia artificial, sino lógica basada en reglas de negocio.

---

## 📈 Valor de Negocio

* Reducción de riesgos operacionales
* Disminución de errores manuales
* Mejora en tiempos de validación
* Base para evolución a soluciones reales

---

## 🔮 Próximos pasos

* Integración con APIs externas
* IA para evaluación de riesgo
* Integración con IoT
* Evolución arquitectónica

---

## 👤 Autor

**Verónica Maldonado Céspedes**
Cloud & DevOps Delivery Manager
Project Manager | Transformación Digital

