from decimal import *
import numpy as np
import sys

def expression_result(val1, val2, op):
  if op == '+': return val1 + val2
  elif op == '-': return val1 - val2
  elif op == '*': return val1 * val2
  elif op == '/': return val1 / val2

expression = ' '.join(sys.argv[1:])

val1, op, val2 =  expression.split(' ')

setcontext(ExtendedContext)
getcontext().Emax = 38
getcontext().Emin = -38

val1 = Decimal(val1)
val2 = Decimal(val2)
result = Decimal(expression_result(val1, val2, op))

print(f'Recebi {val1:.6f} {op} {val2:.6f} e resultado deu {result}')
print(f'val1 = {np.binary_repr(np.float32(val1).view(np.uint32))} = {val1}')
print(f'val2 = {np.binary_repr(np.float32(val2).view(np.uint32))} = {val2}')
print(f'res  = {np.binary_repr(np.float32(result).view(np.uint32))} = {result}')

context = getcontext().flags

print(f'Exeção FE_INEXACT: {context.get(Inexact)}')
print(f'Exeção FE_DIVBYZERO: {context.get(DivisionByZero)}')
print(f'Exeção FE_UNDERFLOW: {context.get(Underflow)}')
print(f'Exeção FE_OVERFLOW: {context.get(Overflow)}')
print(f'Exeção FE_INVALID: {context.get(InvalidOperation)}')
