import re
from decimal import *
import numpy as np
import sys
#pack and unpack -> 
#   extended content set context
# sys argv 


def expression_result(value_1, value_2, operator):
  if operator == '+': return value_1 + value_2
  elif operator == '-': return value_1 - value_2
  elif operator == '*': return value_1 * value_2
  elif operator == '/': return value_1 / value_2

expression = ''.join(sys.argv[1:])
# print(expression)

# def validate_input(expression):  
val1, op, val2 = re.split(r"(\+|\-|\*|\/)", expression)
val1 = Decimal(val1)
val2 = Decimal(val2)

result = expression_result(val1, val2, op)
# print(validate_input(expressao))

print(f'Recebi {val1} {op} {val2} e resultado deu {result}')
print(f'val1 = {np.binary_repr(np.float32(val1).view(np.uint32))} = {val1}')
print(f'val2 = {np.binary_repr(np.float32(val2).view(np.uint32))} = {val2}')
print(f'res  = {np.binary_repr(np.float32(result).view(np.uint32))} = {result}')




# print(val1, val2, op)