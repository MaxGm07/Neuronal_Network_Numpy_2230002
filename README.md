# 💡 Red Neuronal con NumPy 🧩

![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen)

:octocat:

**Estudiante**: Carlos Maximiliano García Medina

**Tarea 3**: Red Neuronal con Numpy

**Materia**: Sistemas de Visión Artificial  


---

## 📝 Descripción

Este repositorio contiene la implementación de una **red neuronal desde cero** utilizando **NumPy** para clasificar datos generados a partir de distribuciones gaussianas. El proyecto incluye:

- 🧩 **Generación de datos**: Creación de un conjunto de datos sintético para clasificación binaria.
- 🛠️ **Construcción de la red neuronal**: Implementación de una red con múltiples capas y funciones de activación.
- 🚀 **Entrenamiento y evaluación**: Entrenamiento de la red neuronal y visualización de los resultados.

El código está comentado paso a paso para una mayor comprensión.

---

## 📋 Requisitos

Para ejecutar este proyecto, necesitas tener instaladas lo siguiente:
- **Python**: 
- [Python 3.8 o superior](https://www.python.org/downloads/)

Se puede comprobar la versión de python empleando el comando en terminal:

**En PowerShell:**

**En Unix**

Librerías (dependencias):
- **NumPy**: Para cálculos numéricos y manejo de arreglos.
- **Matplotlib**: Para la generación de gráficas.
- **Scikit-learn**: Para generar datos sintéticos.

Puedes instalar en conjunto estas dependencias utilizando `pip`:

```bash
pip install numpy matplotlib scikit-learn
```
**Nota:** Si en Unix (Linux) no funciona, emplea ```pip3```

## 🗂️ Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

``` bash
TAREA_3/
│
├── src/
│   └── Neuronal_Network_Numpy.py  # Script principal de la red neuronal
│
├── .gitignore      # Archivo para ignorar archivos no deseados
├── main.py         # Script principal para ejecutar el proyecto
├── README.md       # Este archivo
└── requirements.txt # Lista de dependencias del proyecto
```
## 🚀 ¿Cómo usar este repositorio?
Sigue estos pasos para ejecutar el proyecto en tu lab:

### Clona el repositorio 🖥️:
Abre una terminal y ejecuta el siguiente comando para clonar el repositorio en tu computadora:

```bash
git clone https://github.com/MaxGm07/Neuronal_Network_Numpy_2230002
```
### Cree un nuevo entorno virtual
Se recomienda tener el entorno virtual generado en la carpeta principal para un fácil acceso, su activación y desactivación se realiza de la siguiente forma:

En PowerShell:
```
.\nombre_del_entorno\Scripts\Activate
deactivate
```
En Unix:
```
source nombre_del_entorno/bin/activate
deactivate
```
### Instala las dependencias 📦:
Asegúrate de tener instaladas las bibliotecas necesarias. Ejecuta el siguiente comando para instalarlas:

```bash
pip install -r Requirements.txt
```
### Ejecuta el script principal🚀:
Para entrenar y evaluar la red neuronal, ejecuta:

```bash
python main.py
```
### Visualiza los resultados 📊:

  * El script mostrará el error durante el entrenamiento en la consola.

  * También se mostrará un gráfico con los datos originales y los datos clasificados por la red neuronal. 

## 🛠️ Tecnologías Utilizadas
**Python**: Lenguaje de programación principal en este caso se utilizó la versión 3.11 para el desarrollo del proyecto.

**NumPy**: Para cálculos numéricos y manejo de arreglos.

**Matplotlib**: Para visualización de datos y gráficos.

**Scikit-learn**: Para generar datos sintéticos.

## 🧑‍💻 ¿Qué hace el código?
El código realiza lo siguiente:

1. **Genera un conjunto de datos sintético** utilizando distribuciones gaussianas.
 
2. **Define funciones de activación**:

    * **Sigmoid**: Para la capa de salida.

    * **ReLU**: Para las capas ocultas.

3. **Inicializa los parámetros** de la red neuronal (pesos y sesgos).

4. **Entrena la red neuronal** utilizando propagación hacia adelante y hacia atrás.

5. **Evalúa el modelo** clasificando nuevos datos y visualizando los resultados.

## Notas extra
¡Gracias por llegar al final del readme, espero tengas un buen día!