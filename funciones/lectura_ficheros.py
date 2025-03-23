from funciones.diccionarios import dicc_polinomio

def leer_ficheros(nombre_archivo):
    polinomios = []
    valor_x = None  # Para la evaluación

    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                linea = linea.strip() #Elimina espacios en blanco
                if linea.startswith("x="):  # Si la línea empieza con el valor de x
                    valor_x = float(linea.split("=")[1])  # Extrae el número de x
                else:
                    polinomio = dicc_polinomio(linea)  # Convertirlo a diccionario
                    polinomios.append(polinomio)

    except FileNotFoundError:
        print(" El archivo no existe. Crea un archivo y agrégale polinomios.")
    except Exception as e:
        print(f" Error al leer el archivo: {e}")

    return polinomios, valor_x  # Devuelve los polinomios y el valor de x si existe