# Clasificación de Riesgo de Inundación en Parroquias del Ecuador

**Institución:** Universidad de Guayaquil

**Facultad:** Ciencias Matemáticas y Físicas

**Carrera:** Ingeniería en Ciencia de Datos e Inteligencia Artificial

**Asignatura:** Aprendizaje Automático

**Docente:** Ing. Miguel Botto

**Fecha:** 15 de Febrero, 2026

## Integrantes del Grupo
* Mayerly Kristel Veloz Alburquerque
* Karla Patricia Solórzano Parra
* Juren David Rodríguez Bautista
* Byron Zosimo Tenorio Ferrer

---

## Acceso al Proyecto
**Aplicación web desplegada:** [http://jurenhino.pythonanywhere.com/](http://jurenhino.pythonanywhere.com/)

---

## 1. Descripción del Proyecto
Este proyecto desarrolla un sistema de clasificación supervisada para estimar el nivel de riesgo de inundación (**Alto, Medio, Bajo**) a nivel parroquial en Ecuador. La solución integra variables topográficas y climáticas provenientes de fuentes oficiales (INEC, HDX, OpenTopography) para apoyar la toma de decisiones preventivas.

El sistema final consta de dos componentes principales:
1.  **Modelo de Machine Learning:** Un ensamblaje (Voting Classifier) optimizado para maximizar el *Recall*, garantizando la detección de zonas vulnerables.
2.  **Aplicación Web (Flask):** Una interfaz geoespacial interactiva que permite visualizar los resultados del modelo sobre el territorio nacional.

## 2. Contenido del Repositorio

### Código Fuente y Despliegue
* `app.py`: Backend desarrollado en Flask. Gestiona la lógica del servidor y la renderización del mapa.
* `parroquias.json`: Archivo GeoJSON optimizado con la geometría de las parroquias.
* `DATA_MAPA_FINAL_CON_SCORES.csv`: Dataset procesado que contiene los resultados del modelo (Categoría de Riesgo y Probabilidad).
* `requirements.txt`: Lista de dependencias necesarias para la ejecución (Flask, Folium, Pandas, Gunicorn).

### Ciencia de Datos (Entrenamiento)
* `Proyecto 2Parcia_Riesgo de Inundación en Parroquias.ipynb`: **Jupyter Notebook principal.** Documenta todo el ciclo de vida del proyecto:
    * **Preprocesamiento:** Limpieza de datos y tratamiento de valores nulos.
    * **Ingeniería de Características:** Creación de variables derivadas (Índice de pendiente proxy).
    * **Análisis Exploratorio (EDA):** Visualización de distribución de variables.
    * **Modelado:** Entrenamiento y evaluación comparativa de algoritmos (Regresión Logística, SVM, Random Forest, Voting Classifier).
    * **Evaluación:** Análisis de matrices de confusión y métricas de Recall/F1-Score.

---

## 3. Instrucciones de Ejecución Local

Si desea ejecutar esta aplicación en un entorno local:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Jurenhino/proyecto-riesgo-inundaciones
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```

4.  **Visualizar:**
    Abra su navegador en `http://127.0.0.1:5000/`

---

## 4. Metodología del Modelo
Se evaluaron múltiples algoritmos supervisados para resolver el problema de clasificación multiclase. El modelo seleccionado fue un **Soft Voting Classifier** que combina las predicciones de:
* Regresión Logística
* Support Vector Machine (SVM)
* Random Forest (Optimizado)

**Métrica de Éxito:** Dado el contexto de desastres naturales, se priorizó la maximización del **Recall (Sensibilidad)** para minimizar los falsos negativos (es decir, evitar clasificar una zona de "Alto Riesgo" como segura).

---
© 2026 - Proyecto Académico UG.
