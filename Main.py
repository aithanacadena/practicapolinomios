def dicc_polinomio(polinomio_str):

    polinomio = {}
    polinomio_str = polinomio_str.replace(" ", "")  # Quitamos espacios

    # Separar los términos por los signos + y - manteniendo los signos
    terminos = []
    temp = ""
    for char in polinomio_str:
        if char in "+-" and temp:
            terminos.append(temp)  # Guardamos el término anterior
            temp = char  # Nuevo término empieza con el signo
        else:
            temp += char
    terminos.append(temp)  # Último término

    # Procesar cada término
    for termino in terminos:
        if "x" in termino:  # Términos con x
            coeficiente, _, grado = termino.partition("x^")  # Separar coef y grado

            if grado == "":
                if "x" in coeficiente:
                    coeficiente, _, _ = coeficiente.partition("x")
                    grado = 1
                else:
                    grado = 1
            else:
                grado = int(grado)  # Convertimos grado a número

            if coeficiente in ["", "+"]:  # "+x" es 1x
                coeficiente = 1
            elif coeficiente == "-":  # "-x" es -1x
                coeficiente = -1
            else:
                coeficiente = int(coeficiente)  # Convertimos coeficiente a número

        else:  # Si es solo un número, es un término independiente (grado 0)
            coeficiente = int(termino)
            grado = 0

        polinomio[grado] = polinomio.get(grado, 0) + coeficiente  # Sumar coef en caso de repetidos

    return polinomio


def mostrar_menu():
    print("\n📌 CALCULADORA DE POLINOMIOS")
    print("1️⃣ Introducir polinomios manualmente")
    print("2️⃣ Realizar operaciones con los polinomios")
    print("3️⃣ Salir")


def ingresar_polinomio():
    polinomio_str = input("\n Introduce el polinomio (Ejemplo: 2x^4 + x - 2): ")
    return dicc_polinomio(polinomio_str)  # Convertimos a diccionario aquí mismo


def main():
    polinomios = []  # Guardará los polinomios como diccionarios

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            polinomio = ingresar_polinomio()
            polinomios.append(polinomio)
            print(f"✅ Polinomio guardado: {polinomio}")

        from operaciones import suma_polinomios  # Importamos la función de suma
        from operaciones import restar_polinomios # Importamos la de la resta
        from operaciones import multiplicar_polinomios #Importamos la función que multiplicación

        elif opcion == "2":
            if len(polinomios) < 2:
                print("❌ Debes introducir al menos dos polinomios para poder operar.")
            else:
                print("\n🔹 Escoge una operación:")
                print("1️⃣ Suma")
                print("2️⃣ Resta")
                print("3️⃣ Multiplicación")
                print("4️⃣ División")
                print("5️⃣ Evaluación")

                operacion = input("Selecciona la operación: ")
                # Aquí llamarán a las funciones específicas en cada rama
                if operacion == "1":  # SUMA
                    resultado = suma_polinomios(polinomios[0], polinomios[1])
                    print(f"✅ Resultado de la suma: {resultado}")

                elif operacion == "2":  # RESTA
                    resultado = restar_polinomios(polinomios[0], polinomios[1])
                    print(f"✅ Resultado de la resta: {resultado}")

                elif operacion == "3":  # MULTIPLICACIÓN
                    resultado = multiplicar_polinomios(polinomios[0], polinomios[1])
                    print(f"✅ Resultado de la multiplicación: {resultado}")

        elif opcion == "3":
            print("👋 Saliendo de la calculadora. ¡Adioooós!")
            break

        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()