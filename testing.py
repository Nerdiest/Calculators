import config
from memory_profiler import profile
def chudnovsky(n):
    from algorithms.Chudnovsky.main import Chudnovsky
    init = Chudnovsky([n])
    return init.get()

@profile
def fibonacci(n):
    from algorithms.Fibonacci.main import Fibonacci
    init = Fibonacci([n])
    return init.get()

@profile
def largepower(a, b):
    from algorithms.LargePower.main import LargePower
    init = LargePower([a,b])
    return init.get()

@profile
def eulerstotient(n):
    from algorithms.EulersTotient.main import EulersTotient
    init = EulersTotient([n])
    return init.get()


print(eulerstotient(13))


