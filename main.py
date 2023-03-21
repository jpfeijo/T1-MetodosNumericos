import re
from decimal import *
import numpy as np
import sys
#pack and unpack -> 
#   extended content set context

def expression_result(value_1, value_2, operator):
  if operator == '+': return value_1 + value_2
  elif operator == '-': return value_1 - value_2
  elif operator == '*': return value_1 * value_2
  elif operator == '/': return value_1 / value_2

expression = ' '.join(sys.argv[1:])

val1, op, val2 =  expression.split(' ')

val1 = Decimal(val1)
val2 = Decimal(val2)
result = Decimal(expression_result(val1, val2, op))

print(f'Recebi {val1:.6f} {op} {val2:.6f} e resultado deu {result}')
print(f'val1 = {np.binary_repr(np.float32(val1).view(np.uint32))} = {val1}')
print(f'val2 = {np.binary_repr(np.float32(val2).view(np.uint32))} = {val2}')
print(f'res  = {np.binary_repr(np.float32(result).view(np.uint32))} = {result}')
