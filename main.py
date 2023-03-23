from decimal import *
import numpy as np
import sys

def expression_result(val1, val2, op):
  if op == '+': return val1 + val2
  elif op == '-': return val1 - val2
  elif op == '*': return val1 * val2
  elif op == '/': return val1 / val2

def print_binary_ieee754(num_bin, num):
  num_str = str(num_bin)
  if str(num)[0] == '-':
    return f'{num_str[0]} {num_str[1:9]} {num_str[9:]}'
  else:
    return f'{0} {num_str[0:8]} {num_str[8:]}'

expression = ' '.join(sys.argv[1:])

val1, op, val2 =  expression.split(' ')

setcontext(ExtendedContext)
getcontext().Emax = 38
getcontext().Emin = -38

val1 = Decimal(val1)
val1_bin = np.binary_repr(np.float32(val1).view(np.uint32))

val2 = Decimal(val2)
val2_bin = np.binary_repr(np.float32(val2).view(np.uint32))

result = Decimal(expression_result(val1, val2, op))
result_bin = np.binary_repr(np.float32(result).view(np.uint32))

print(f'Recebi {val1:.6f} {op} {val2:.6f} e resultado deu {result}')
print(f'val1 = {print_binary_ieee754(val1_bin, val1)} = {val1}')
print(f'val2 = {print_binary_ieee754(val2_bin, val2)} = {val2}')
print(f'res  = {print_binary_ieee754(result_bin, result)} = {result}')

context = getcontext().flags

print(f'Exeção FE_INEXACT: {context.get(Inexact)}')
print(f'Exeção FE_DIVBYZERO: {context.get(DivisionByZero)}')
print(f'Exeção FE_UNDERFLOW: {context.get(Underflow)}')
print(f'Exeção FE_OVERFLOW: {context.get(Overflow)}')
print(f'Exeção FE_INVALID: {context.get(InvalidOperation)}')
