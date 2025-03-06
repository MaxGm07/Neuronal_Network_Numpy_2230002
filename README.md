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

## Explicación del código
El código realiza lo siguiente:

1. **Genera un conjunto de datos sintético** utilizando distribuciones gaussianas.
 
2. **Define funciones de activación**:

    * **Sigmoid**: Para la capa de salida.

    * **ReLU**: Para las capas ocultas.

3. **Inicializa los parámetros** 
  
Los pesos (weights) y sesgos (biases) de la red neuronal se inicializan aleatoriamente.

Para una red con una capa oculta de n neuronas y una capa de salida de m neuronas:

    Pesos de la capa oculta: W1 (matriz de tamaño n_features x n)

    Sesgos de la capa oculta: b1 (vector de tamaño 1 x n)

    Pesos de la capa de salida: W2 (matriz de tamaño n x m)

    Sesgos de la capa de salida: b2 (vector de tamaño 1 x m)

4. **Entrena la red neuronal** utilizando propagación hacia adelante y hacia atrás.

En esta fase, los datos de entrada se propagan a través de la red para obtener las predicciones.

Pasos:
-(Forward Propagation)
    Multiplicar las entradas por los pesos y sumar los sesgos.

    Aplicar la función de activación ReLU en la capa oculta.

    Multiplicar la salida de la capa oculta por los pesos de la capa de salida y sumar los sesgos.

    Aplicar la función de activación Sigmoid en la capa de salida.

-(Loss)
  Se utiliza la función de pérdida de entropía cruzada binaria (binary cross-entropy) para medir el error entre las predicciones y las etiquetas reales.

-(Backpropagation)
En esta fase, se calculan los gradientes de la pérdida con respecto a los pesos y sesgos para actualizarlos.

    Calcular el gradiente de la pérdida con respecto a la salida (dA2).

    Calcular el gradiente de la pérdida con respecto a Z2 (capa de salida).

    Calcular los gradientes de W2 y b2.

    Calcular el gradiente de la pérdida con respecto a A1.

    Calcular el gradiente de la pérdida con respecto a Z1 (capa oculta).

    Calcular los gradientes de W1 y b1.

Por último se actualizan los pesos y sesgos mediante el algoritmo del gradiente descendiente.
Posterior a ello, la red neuronal se entrena mediante épocas definidas en el código

5. **Evalúa el modelo** clasificando nuevos datos y visualizando los resultados.

## Notas extra
¡Gracias por llegar al final del readme, agradezco tu tiempo, espero tengas un buen día!