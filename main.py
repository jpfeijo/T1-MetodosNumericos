import re

expressao = input('Expressão: ')

val1, operador, val2 = re.split(r"(\+|\-|\*|\/)", expressao)
val1 = float(val1)
val2 = float(val2)

print(val1, val2, operador)