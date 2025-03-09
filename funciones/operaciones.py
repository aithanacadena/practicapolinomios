def suma_polinomios(p1, p2):

    resultado = p1.copy()

    for grado, coef in p2.items():
        resultado[grado] = resultado.get(grado, 0) + coef

    return resultado
