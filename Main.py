from funciones.operaciones import suma_polinomios
from funciones.operaciones import restar_polinomios
from funciones.operaciones import multiplicar_polinomios
from funciones.operaciones import dividir_polinomios
from funciones.operaciones import evaluar_polinomio

def dicc_polinomio(polinomio_str):
    polinomio = {}
    polinomio_str = polinomio_str.replace(" ", "")

    terminos = []
    temp = ""
    for char in polinomio_str:
        if char in "+-" and temp:
            terminos.append(temp)
            temp = char
        else:
            temp += char
    terminos.append(temp)

    for termino in terminos:
        if "x" in termino:
            coeficiente, _, grado = termino.partition("x^")

            if grado == "":
                if "x" in coeficiente:
                    coeficiente, _, _ = coeficiente.partition("x")
                    grado = 1
                else:
                    grado = 1
            else:
                grado = int(grado)

            if coeficiente in ["", "+"]:
                coeficiente = 1
            elif coeficiente == "-":
                coeficiente = -1
            else:
                coeficiente = int(coeficiente)

        else:
            coeficiente = int(termino)
            grado = 0

        polinomio[grado] = polinomio.get(grado, 0) + coeficiente

    return polinomio


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

            operacion = input("⚡ Selecciona la operación: ")

            if operacion in ["1", "2", "3", "4"]:
                print("\n Introduce los dos polinomios para operar:")
                polinomio1 = ingresar_polinomio()
                polinomio2 = ingresar_polinomio()

                if operacion == "1":
                    resultado = suma_polinomios(polinomio1, polinomio2)
                    print(f"✅ Resultado de la suma: {resultado}")

                elif operacion == "2":
                    resultado = restar_polinomios(polinomio1, polinomio2)
                    print(f"✅ Resultado de la resta: {resultado}")

                elif operacion == "3":
                    resultado = multiplicar_polinomios(polinomio1, polinomio2)
                    print(f"✅ Resultado de la multiplicación: {resultado}")

                elif operacion == "4":
                    resultado = dividir_polinomios(polinomio1, polinomio2)
                    print(f"✅ Resultado de la división: {resultado}")

            elif operacion == "5":
                print("\n Introduce el polinomio a evaluar:")
                polinomio = ingresar_polinomio()
                x = float(input(" Introduce el valor de x: "))
                resultado = evaluar_polinomio(polinomio, x)
                print(f"✅ Resultado de la evaluación: {resultado}")

            else:
                print("❌ Opción no válida.")

        elif opcion == "2":
            print(" Funcionalidad de lectura de ficheros pendiente de implementar.")

        elif opcion == "3":
            print("Apagando calculadora...")
            break

        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()