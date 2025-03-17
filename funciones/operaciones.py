# SUMA
def suma_polinomios(p1, p2):

    resultado = p1.copy()

    for grado, coef in p2.items():
        resultado[grado] = resultado.get(grado, 0) + coef

    return resultado

# RESTA
def restar_polinomios(p1, p2):

    resultado = p1.copy()

    for grado, coef in p2.items():
        resultado[grado] = resultado.get(grado, 0) - coef

    return resultado

## MULTIPLICACIÓN
def multiplicar_polinomios(p1, p2):
    resultado = {}

    for grado1, coef1 in p1.items():
        for grado2, coef2 in p2.items():
            nuevo_grado = grado1 + grado2
            nuevo_coef = coef1 * coef2

            if nuevo_grado in resultado:
                resultado[nuevo_grado] += nuevo_coef
            else:
                resultado[nuevo_grado] = nuevo_coef

    return resultado

# DIVISIÓN
def dividir_polinomios(dividendo, divisor):

    if not divisor:
        raise ValueError("El divisor no puede ser un polinomio vacío.")

    # Obtener el grado máximo de ambos polinomios
    grado_dividendo = max(dividendo.keys(), default=0)
    grado_divisor = max(divisor.keys(), default=0)

    # Si el grado del dividendo es menor que el del divisor, la división no es posible
    if grado_dividendo < grado_divisor:
        return ({}, dividendo)  # El cociente es 0 y el residuo es el dividendo

    cociente = {}

    # Copia del dividendo para ir restando los múltiplos del divisor
    resto = dividendo.copy()

    while resto and max(resto.keys()) >= grado_divisor:
        # Obtener el término líder del dividendo y del divisor
        grado_resto = max(resto.keys())
        coef_resto = resto[grado_resto]

        grado_cociente = grado_resto - grado_divisor
        coef_cociente = coef_resto / divisor[grado_divisor]

        # Agregar el término al cociente
        cociente[grado_cociente] = coef_cociente

        # Crear el polinomio a restar
        polinomio_a_restar = {
            grado + grado_cociente: coef * coef_cociente
            for grado, coef in divisor.items()
        }

        # Restar el polinomio obtenido del resto
        for grado, coef in polinomio_a_restar.items():
            if grado in resto:
                resto[grado] -= coef
                if abs(resto[grado]) < 1e-10:  # Para evitar problemas con flotantes
                    del resto[grado]
            else:
                resto[grado] = -coef

    return (cociente, resto)

