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

