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


print(fibonacci(100000))


