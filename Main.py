def mostrar_menu():
    print("\nCALCULADORA DE POLINOMIOS")
    print("1 Introducir polinomios manualmente")
    print("2 Realizar operaciones con los polinomios")
    print("3 Salir")


def ingresar_polinomio():
    polinomio = input("Introduce el polinomio (Ejemplo: 2x^4 + x - 2): ")
    return polinomio


def main():
    polinomios = []  # Lista para almacenar los polinomios ingresados

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            polinomio = ingresar_polinomio()
            polinomios.append(polinomio)
            print(f"✅ Polinomio guardado: {polinomio}")

        elif opcion == "2":
            if len(polinomios) < 2:
                print("❌ Debes introducir al menos dos polinomios para operar.")
            else:
                print("Escoge una operación:")
                print("1 Suma")
                print("2 Resta")
                print("3 Multiplicación")
                print("4 División")
                print("5 Evaluación")

                operacion = input("Selecciona la operación: ")
                # Aquí llamarán a las funciones específicas en cada rama
                print("Función de operación pendiente de implementación.")

        elif opcion == "3":
            print("Saliendo de la calculadora. ¡Adioooós!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()