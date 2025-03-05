
cat << 'EOF' > README.md
# Red Neuronal con NumPy

![Badge](https://img.shields.io/badge/Estado-Completado-brightgreen)

:octocat:

Este repositorio contiene una implementación de una **red neuronal simple** desde cero utilizando **NumPy**. El proyecto es parte del curso **visión artificial** y se enfoca en comprender los conceptos fundamentales de las redes neuronales, incluyendo la propagación hacia adelante, la retropropagación y el descenso de gradiente.

## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Estructura del Proyecto](#estructura-del-proyecto)


---

## Descripción

Este proyecto es una implementación de una **red neuronal básica** utilizando únicamente **NumPy**. El objetivo es proporcionar una comprensión clara de cómo funcionan las redes neuronales, desde la propagación hacia adelante hasta la retropropagación y la optimización mediante el descenso de gradiente. Este repositorio incluye el código fuente, documentación y ejemplos para facilitar el aprendizaje y la experimentación.

---

## Características

- **Arquitectura Personalizable**: Define el número de capas y neuronas por capa.
- **Propagación hacia Adelante**: Implementada utilizando operaciones matriciales en NumPy.
- **Retropropagación**: Cálculo eficiente de los gradientes para la actualización de los pesos.
- **Funciones de Activación**: Soporta funciones de activación comunes como ReLU, Sigmoide y Tanh.
- **Descenso de Gradiente**: Optimiza la red utilizando el descenso de gradiente.
- **Código Modular**: Fácil de extender y modificar para experimentación.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.8 o superior](https://www.python.org/downloads/)
- [NumPy](https://numpy.org/install/)

Se recomienda crear un entorno virtual para probar el código principal. Puedes hacerlo con los siguientes comandos:

**En PowerShell:**
```bash
python -m venv nombre_del_entorno
```
**En Unix:**
```bash
python3 -m venv nombre_del_entorno
```
---
## Instalación

Sigue estos pasos para clonar y configurar el proyecto en tu máquina local:

1. Clona este repositorio:
        git clone https://github.com/MaxGm07/Neuronal_Network_Numpy_2230002.git
        cd Neuronal_Network_Numpy_2230002
2. Crea un nuevo entorno virtual (se describe mejor el procedimiento en el apartado de Nota).
3. Instala las dependencias requeridas (recomendado: dentro del entorno virtual):
    pip install -r requirements.txt

Nota: En Unix, usa pip3 en lugar de pip.

---
## Nota para el entorno virtual
Se recomienda tener el entorno virtual generado en la carpeta principal para un fácil acceso. Su activación y desactivación se realiza de la siguiente forma:

**En PowerShell:**
    .\nombre_del_entorno\Scripts\Activate
    deactivate

**En Unix:**
    source nombre_del_entorno/bin/activate
    deactivate
---
## Uso
Finalmente, para emplear este repositorio, con sus respectivos requerimientos y entorno virtual cumplidos, se puede proceder a usar el código main.py mediante los siguientes comandos:
**En PowerShell**
    python main.py

**En Unix**
    python3 main.py

## Estructura del proyecto
Neuronal_Network_Numpy_2230002/
├── neural_network.py       # Implementación principal de la red neuronal
├── activation_functions.py # Contiene funciones de activación y sus derivadas
├── utils.py                # Funciones de utilidad para preprocesamiento de datos
├── main.py                 # Código principal para entrenar y probar la red
├── README.md               # Este archivo
└── requirements.txt        # Lista de dependencias
