# SUMA
def suma_polinomios(p1, p2):

    resultado = p1.copy() # Para no sobreescribir en p1

    for grado, coef in p2.items(): # Lista de parejas (grado, coef)
        resultado[grado] = resultado.get(grado, 0) + coef # Suma los coeficientes del mismo grado

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
        # default = 0, por si el dividendo es 0, que devuelva 0 como grado máximo


    # Si el grado del dividendo es menor que el del divisor, la división no es posible
    if grado_dividendo < grado_divisor:
        return ({}, dividendo)  # El cociente es 0 y el resto es el dividendo

    cociente = {}

    # Copia del dividendo para ir restando los múltiplos del divisor
    resto = dividendo.copy()
# Dividimos mientras haya términos en el resto, y su grado sea al menos el del divisor
    while resto and max(resto.keys()) >= grado_divisor:
        # Obtener el valor del resto que tiene asignado el máximo grado
        grado_resto = max(resto.keys())
        coef_resto = resto[grado_resto]

        # Dividimos el término con mayor grado del resto entre el término con mayor grado del divisor
        grado_cociente = grado_resto - grado_divisor # Se restan los exponentes
        coef_cociente = coef_resto / divisor[grado_divisor] # Se dividen los coeficientes

        # Agregar el término que acabamos de obtener al cociente
        cociente[grado_cociente] = coef_cociente

        # Crear el polinomio a restar
        # Construye un nuevo polinomio que será restado del "resto" en la división de polinomios
        # Multiplicando el divisor por el término recién encontrado
        polinomio_a_restar = {
            grado + grado_cociente: coef * coef_cociente
            for grado, coef in divisor.items()
        }

        # Restar el polinomio obtenido del resto
        for grado, coef in polinomio_a_restar.items():
            if grado in resto:
                resto[grado] -= coef # Si el término está en el resto, lo restamos
                if abs(resto[grado]) < 1e-10:  # Para evitar problemas con flotantes
                    del resto[grado] # Si se vuelve cero, lo eliminamos
            else:
                resto[grado] = -coef # Si no está, lo agregamos con el signo opuesto

    return (cociente, resto)

## EVALUCIACIÓN
def evaluar_polinomio(polinomio, x):
    resultado = sum(coef * (x ** grado) for grado, coef in polinomio.items())
    return resultado

