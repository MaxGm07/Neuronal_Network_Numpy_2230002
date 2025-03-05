
# Red Neuronal con NumPy

![Badge](https://img.shields.io/badge/Estado-Completado-brightgreen)

:octocat:

Este repositorio contiene una implementación de una **red neuronal simple** desde cero utilizando **NumPy**. El proyecto es parte del curso **Visión Artificial** y se enfoca en comprender los conceptos fundamentales de las redes neuronales, incluyendo la propagación hacia adelante, la retropropagación y el descenso de gradiente.

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [Contribuir](#contribuir)
8. [Licencia](#licencia)

## Descripción
Este proyecto es una implementación de una **red neuronal básica** utilizando únicamente **NumPy**. Su objetivo es proporcionar una comprensión clara de cómo funcionan las redes neuronales, desde la propagación hacia adelante hasta la retropropagación y la optimización mediante el descenso de gradiente. Este repositorio incluye el código fuente, documentación y ejemplos para facilitar el aprendizaje y la experimentación.

## Características
- **Arquitectura Personalizable**: Permite definir el número de capas y neuronas por capa.
- **Propagación hacia Adelante**: Implementada utilizando operaciones matriciales en NumPy.
- **Retropropagación**: Cálculo eficiente de los gradientes para la actualización de los pesos.
- **Funciones de Activación**: Compatible con ReLU, Sigmoide y Tanh.
- **Descenso de Gradiente**: Implementado para optimizar la red.
- **Código Modular**: Fácil de extender y modificar.

## Requisitos
Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- [Python 3.8 o superior](https://www.python.org/downloads/)
- [NumPy](https://numpy.org/install/)

Se recomienda crear un entorno virtual para aislar las dependencias del proyecto:
```bash
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate

# En Unix (Linux/macOS)
python3 -m venv venv
source venv/bin/activate
```

## Instalación
Sigue estos pasos para configurar el proyecto en tu máquina local:
```bash
git clone https://github.com/MaxGm07/Neuronal_Network_Numpy_2230002.git
cd Neuronal_Network_Numpy_2230002
pip install -r requirements.txt
```
Si usas Unix, usa `pip3` en lugar de `pip`.

## Uso
Ejecuta el siguiente comando para entrenar y evaluar la red neuronal:
```bash
python3 main.py
```

## Estructura del Proyecto
```bash
Neuronal_Network_Numpy_2230002/
├── neural_network.py  # Implementación principal de la red neuronal
├── activation_functions.py  # Funciones de activación y sus derivadas
├── utils.py  # Funciones auxiliares para preprocesamiento de datos
├── main.py  # Código principal para entrenar y probar la red
├── README.md  # Este archivo
└── requirements.txt  # Lista de dependencias
```

## Contribuir
Las contribuciones son bienvenidas. Para colaborar con el proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -m 'Descripción del cambio'`).
4. Sube los cambios a tu fork (`git push origin nueva-funcionalidad`).
5. Abre un Pull Request en este repositorio.
