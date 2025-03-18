# **CALCULADORA DE POLINOMIOS EN PYTHON**


### **Descripción:**

Este proyecto es una calculadora de polinomios hecha en Python que permite
realizar diversas operaciones matemáticas con polinomios. 

### **Funciones de la calculadora:**

1. Suma de polinomios 
2. Resta de polinomios 
3. Multiplicación de polinomios
4. División de polinomios
5. Evaluación de un polinomio en un valor dado

La calculadora es interactiva y permite introducir los polinomios por pantalla o 
por fichero para realizar las operaciones. Está diseñada para cualquier persona que 
necesite trabajar con polinomios, ya que es muy intuitiva, tanto estudiantes como desarrolladores 
que quieran automatizar cálculos algebraicos. 


### **Instalación:** 

Este proyecto no necesita librerias externas, solo necesitas Python instalado en tu ordenador. 

### **Requisitos:** 
- Python 3.8 o superior
- Un editor de código como PyCharm, VS Code o ejecutar en la terminal

### **Cómo instalarlo:**

Clonar el repositório:

git clone 
https://github.com/aithanacadena/practicapolinomios

### **Uso de la calculadora:** 

Cuando ejecutas el programa, verás un menú con varias opciones.

Ejemplo de uso:
1. Realizar operaciones con los polinomios
2. Leer fichero con operaciones
3. Salir

##### Al seleccionar la opción 1:

Aparecerá en pantalla un menú con 5 opciones
1. Suma
2. Resta
3. Multiplicación 
4. División
5. Evaluación

Si la opción 1,2,3 o 4 es seleccionada, la calculadora pedirá que ingreses
dos polinomios que serán con los que se realice ya sea la operación de
suma, resta, multiplicación o división según la opción elegida en el menú
anterior.  

Si la opción elegida es la 5, que correspondería a la opción de evaluación,
se pedirá introducir un polinomio y un valor de x que será el que se evaluará
en el polinomio introducido. 

Para introducir los polinomios aparecerá un ejemplo del formato en que se deben introducir.

##### Al seleccionar la opción 2: 

Se pide que ingreses el nombre del  fichero donde estén incluidos tus polinomios , por 
ejemplo polinomios.txt. La calculadora leerá tanto los polinomios que estén en el fichero como 
los valores de "x" para la evaluación. 

Tras esto, aparecerá el menú de operaciones, donde seleccionaras la opción con la operación deseada para hacer
con tus polinomios ingresados en el fichero. 

#### Al seleccionar la opción 3: 

La calculadora se apagará.

#### Formato del resultado obtenido por la calculadora: 

La calculadora esta configurada para hacer las operaciones en tipo diccionario, es decir con una estructura
de {clave:valor}, siendo la clave el grado de cada elemento del polinomio y el valor el número que le corresponde. 
Es decir, si el resultado que nos da la calculadora es: {3: 3, 1: 5, 0: -6} correspondería al polinomio
3x^3 + 5x - 6.

**¡IMPORTANTE!** 
La calculadora no tiene porque devolver el polinomio ordenado de mayor grado a menor grado, es decir, es 
posible que la calculadora devuelva un resultado como {2: 6, 4: 1, 0: 9, 1: 1} para un polinomio con valor de
6x^2 + x^4 + 9 + x

### Autores:

Pablo Blanco-Traba Villar

Aithana Cadena Ospitia 




