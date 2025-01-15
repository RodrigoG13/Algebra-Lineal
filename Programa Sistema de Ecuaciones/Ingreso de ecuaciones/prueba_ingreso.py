uno = "1"
ecuacion_string = input("Ingresa el sistema:")
matriz = []
sin_unomas = "+"
sin_unomenos = "-"
uno_mas = "+1"
uno_menos = "-1"
ecuacion_string = ecuacion_string.lower()
ecuacion_string = ecuacion_string.replace("=", "x")

for a in range(97, 123):
    sin_unomas_letra = sin_unomas + chr(a)
    sin_unomenos_letra = sin_unomenos + chr(a)

    if ecuacion_string.startswith(chr(a)):
        ecuacion_string = uno + ecuacion_string
        ecuacion_string = ecuacion_string.replace(chr(a), "x")

    elif sin_unomas_letra in ecuacion_string:
        uno_mas_letra = uno_mas+"x"
        ecuacion_string = ecuacion_string.replace(sin_unomas_letra, uno_mas_letra)

    elif sin_unomenos_letra in ecuacion_string:
        uno_menos_letra = uno_menos+"x"
        ecuacion_string = ecuacion_string.replace(sin_unomenos_letra, uno_menos_letra)

    elif chr(a) in ecuacion_string:
        ecuacion_string = ecuacion_string.replace(chr(a), "x")

ecuacion_string = ecuacion_string.split("x")
ecuacion_string.remove("")
for numero in ecuacion_string:
    matriz.append(float(numero))
print(matriz)




