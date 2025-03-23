def dicc_polinomio(polinomio_str):
    polinomio = {}
    polinomio_str = polinomio_str.replace(" ", "")

    terminos = []
    temp = ""
    for char in polinomio_str: #Separar los terminos
        if char in "+-" and temp:
            terminos.append(temp)
            temp = char
        else:
            temp += char
    terminos.append(temp)

    for termino in terminos: #Manejo de excepciones en los terminos
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

        polinomio[grado] = polinomio.get(grado, 0) + coeficiente #Si hay dos terminos con el mismo grado los junta

    return polinomio