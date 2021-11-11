# import fibo_yaniv
# print(fibo_yaniv.fib(100))

from fibo_yaniv import fib as fib_yaniv
from fibo_aviel import fib as fib_aviel
from fibo_yaniv import pi

fib_yaniv(100)
fib_aviel(100)

if 100 / pi == 4:
    print("hey")
