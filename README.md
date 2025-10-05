# 🛶 Selección Óptima de Remeros para Competición mediante Técnicas de Optimización Multiobjetivo

Este repositorio contiene los archivos en **Python** y **Jupyter Notebook** utilizados en el modelo de optimización aplicado a la conformación de equipos de remo competitivo, basado en **Programación Lineal (PL)** y **Programación Entera (PE)**.

El proyecto propone el uso de **técnicas de optimización multiobjetivo** para determinar la configuración ideal de un equipo de remo en embarcaciones tipo *Llaüt Valencià*, maximizando el rendimiento y manteniendo el equilibrio lateral de la barca.

---

## 📘 Descripción general

En el remo de competición, la composición del equipo tiene un impacto directo en el rendimiento global y en la estabilidad de la embarcación.  
Este trabajo aplica modelos de optimización matemática para seleccionar la combinación óptima de remeros entre un conjunto de candidatos, considerando factores como:

- **Potencia mecánica** (watts por palada)  
- **Peso corporal** (afecta el balance del bote)  
- **Edad** (relacionada con experiencia y bonificación por categoría)  
- **Técnica** (nivel de coordinación y eficiencia)  
- **Preferencias de posición** (babor o estribor)

El modelo busca maximizar la fuerza total generada, equilibrar los pesos laterales y distribuir correctamente la técnica y la edad promedio del equipo.

---

## ⚙️ Enfoques de optimización utilizados

Se implementaron dos enfoques complementarios de optimización multiobjetivo:

### 1️⃣ Enfoque Secuencial
En este método, las funciones objetivo se resuelven de forma jerárquica.  
Cada etapa fija el valor óptimo de la función anterior antes de optimizar la siguiente:

1. **Maximizar la fuerza total del equipo**  
2. **Maximizar la edad promedio del equipo**  
3. **Minimizar el peso total de la embarcación**  
4. **Minimizar la diferencia de peso entre babor y estribor**

De este modo, el modelo mantiene la máxima fuerza alcanzada y, dentro de esa solución, optimiza los criterios secundarios.

---

### 2️⃣ Enfoque de Suma Ponderada
En este caso, las distintas funciones objetivo se combinan en una sola ecuación escalar ponderada:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{120}Z=w_1\cdot\text{Fuerza}-w_2\cdot\text{Peso}-w_3\cdot D+w_4\cdot\text{Edad}" alt="Fórmula"/>
</p>

Donde los pesos utilizados son:
- \( w_1 = 0.2 \) → Maximizar fuerza total  
- \( w_2 = 0.2 \) → Minimizar peso total  
- \( w_3 = 0.1 \) → Minimizar diferencia lateral  
- \( w_4 = 0.5 \) → Maximizar edad promedio  

Ambos modelos se resolvieron utilizando el **solver CBC** (COIN-OR Branch and Cut), disponible en la librería [`PuLP`](https://coin-or.github.io/pulp/).

---

## 📊 Conjunto de datos

El conjunto de datos utilizado corresponde a un grupo de 13 deportistas anonimizados (`Rower 1` a `Rower 13`), descritos por las siguientes variables:

| Variable | Descripción |
|-----------|-------------|
| **Edad (años)** | Edad al momento de la competición |
| **Peso (kg)** | Masa corporal previa al embarque |
| **Potencia (W)** | Potencia media en test de ergómetro (2.000 m) |
| **Técnica (0–20)** | Nivel técnico y de coordinación |
| **Posiciones preferidas** | Conjunto de posiciones permitidas (B1–B4, E1–E4) |

Las posiciones se agrupan de la siguiente manera:
- **Babor:** B1, B2, B3, B4  
- **Estribor:** E1, E2, E3, E4

---

## 🧮 Formulación matemática

El problema se modela como un sistema de **programación lineal entera binaria (PLEB)**.  
Cada remero puede ocupar solo una posición, y cada posición debe ser ocupada por un único remero.  
El modelo incluye restricciones de:

- Asignación única por remero y posición  
- Restricciones de equilibrio lateral  
- Posiciones preferidas por cada atleta  
- Orden decreciente de técnica en posiciones clave  

La función objetivo busca encontrar la mejor combinación de remeros que maximice la eficiencia global del equipo.

---

## 📈 Resultados

Los modelos desarrollados fueron validados utilizando datos reales del **Club de Rem Dénia**, temporada **2024–2025**, con resultados obtenidos en la **regata de Benidorm (19 de enero de 2025)**.  

Se compararon los resultados de los modelos con el equipo real, observándose:

- Incremento de **+7 % en fuerza total** con el modelo secuencial.  
- Reducción del desbalance lateral de **43 kg a 1 kg**.  
- Ligera mejora en la técnica promedio (+1.6 %).  
- Mantenimiento de un peso y edad promedio similares.

---

## 🧠 Requisitos

- Python ≥ 3.9  
- Librerías:
  - `pulp`
  - `numpy`
  - `matplotlib` *(para visualización de resultados)*

Instalación rápida:

```bash
pip install pulp numpy matplotlib
