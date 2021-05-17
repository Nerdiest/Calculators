from config import limits
from gmpy2 import mpz
from functools import lru_cache


class Fibonacci:
    def __init__(self, n):
        self.n = int(n[0])

    @lru_cache
    def fibonacci(self):
        def fib_inner(n):
            if n == 0:
                return mpz(2), mpz(1)
            m = n >> 1
            u, v = fib_inner(m)
            q = (2, -2)[m & 1]
            u = u * u - q
            v = v * v + q
            if n & 1:
                return v - u, v
            return u, v - u

        m = self.n >> 1
        u, v = fib_inner(m)

        f = (2 * v - u) / 5
        if self.n & 1:
            q = (self.n & 2) - 1
            return v * f - q
        return u * f

    def get(self):
        if self.n > limits['fibonacci']:
            return str(0)
        return str(int(self.fibonacci()))
