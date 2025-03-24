from funciones.operaciones import suma_polinomios #Importamos la función de suma desde operaciones
from funciones.operaciones import restar_polinomios #Importamos la función de resta desde operaciones
from funciones.operaciones import multiplicar_polinomios #Importamos la función de multiplicación desde operaciones
from funciones.operaciones import dividir_polinomios #Importamos la función de división desde operaciones
from funciones.operaciones import evaluar_polinomio #Importamos la función de evaluación desde operaciones
from funciones.lectura_ficheros import leer_ficheros #Importamos la función de lectura de ficheros
from funciones.diccionarios import dicc_polinomio #Importamos la función de diccionarios
from funciones.lectura_ficheros import guardar_resultado_en_fichero #Importamos la función de guardar resultados

def mostrar_menu():
    print("\n CALCULADORA DE POLINOMIOS")
    print("1. Realizar operaciones con los polinomios")
    print("2. Leer fichero de operaciones")
    print("3. Salir")

def ingresar_polinomio():
    polinomio_str = input("\n Introduce el polinomio (Ejemplo: 2x^4 + x - 2): ")
    return dicc_polinomio(polinomio_str)

def main():
    while True:
        mostrar_menu()
        opcion = input(" Selecciona una opción: ")

        if opcion == "1":
            print("\n Escoge una operación:")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Evaluación")

            operacion = input(" Selecciona la operación: ")

            if operacion in ["1", "2", "3", "4"]:
                print("\n Introduce los dos polinomios para operar:")
                polinomio1 = ingresar_polinomio()
                print(f"\n Polinomio 1 guardado correctamente {polinomio1}")
                polinomio2 = ingresar_polinomio()
                print(f"\n Polinomio 2 guardado correctamente {polinomio2}")

                if operacion == "1":
                    resultado = suma_polinomios(polinomio1, polinomio2)
                    print(f" Resultado de la suma: {resultado}")

                elif operacion == "2":
                    resultado = restar_polinomios(polinomio1, polinomio2)
                    print(f" Resultado de la resta: {resultado}")

                elif operacion == "3":
                    resultado = multiplicar_polinomios(polinomio1, polinomio2)
                    print(f" Resultado de la multiplicación: {resultado}")

                elif operacion == "4":
                    resultado = dividir_polinomios(polinomio1, polinomio2)
                    print(f" Resultado de la división: {resultado}")

            elif operacion == "5":
                print("\n Introduce el polinomio a evaluar:")
                polinomio = ingresar_polinomio()
                x = float(input(" Introduce el valor de x: "))
                resultado = evaluar_polinomio(polinomio, x)
                print(f" Resultado de la evaluación: {resultado}")

            else:
                print(" Opción no válida. Inténtelo de nuevo.")

        # Preguntar si quiere guardar el resultado
        if input("¿Quieres guardar el resultado en un archivo? (s/n): ").strip().lower() == "s":
            guardar_resultado_en_fichero(resultado)


        elif opcion == "2":

            nombre_archivo = input(" Introduce el nombre del archivo (Ejemplo: polinomios.txt): ")

            polinomios, valor_x = leer_ficheros(nombre_archivo)

            if not polinomios:

                print(" No se encontraron polinomios en el archivo.")

            else:

                print(f" Polinomios cargados desde archivo: {polinomios} y valor de x: {valor_x}")
                print("\n Escoge una operación:")
                print("1. Suma")
                print("2. Resta")
                print("3. Multiplicación")
                print("4. División")
                print("5. Evaluación")

                operacion = input("Selecciona la operación: ")

                if operacion in ["1", "2", "3", "4"] and len(polinomios) < 2:
                    print(" Se necesitan al menos dos polinomios para operar.")

                elif operacion == "5" and valor_x is None:
                    print(" No se encontró un valor de x en el archivo.")

                else:

                    if operacion == "1":
                        resultado = suma_polinomios(polinomios[0], polinomios[1])
                        print(f" Resultado de la suma: {resultado}")

                    elif operacion == "2":
                        resultado = restar_polinomios(polinomios[0], polinomios[1])
                        print(f" Resultado de la resta: {resultado}")

                    elif operacion == "3":
                        resultado = multiplicar_polinomios(polinomios[0], polinomios[1])
                        print(f" Resultado de la multiplicación: {resultado}")

                    elif operacion == "4":
                        resultado = dividir_polinomios(polinomios[0], polinomios[1])
                        print(f" Resultado de la división: {resultado}")

                    elif operacion == "5":
                        resultado = evaluar_polinomio(polinomios[0], valor_x)
                        print(f" Resultado de la evaluación: {resultado}")

                    # Preguntar si quiere guardar el resultado
                    if input("¿Quieres guardar el resultado en un archivo? (s/n): ").strip().lower() == "s":
                        guardar_resultado_en_fichero(resultado)

        elif opcion == "3":
            print("Apagando calculadora...")
            break

        else:
            print(" Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()