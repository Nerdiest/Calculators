from functools import lru_cache


class LargePower:
    def __init__(self, n):
        self.a = int(n[0])
        self.b = int(n[1])

    @lru_cache
    def compute(self):
        return pow(self.a, self.b, int(1e9+7))

    def get(self):
        if self.a == 0:
            return str(0)
        if self.b == 0:
            return str(1)
        return str(self.compute())
