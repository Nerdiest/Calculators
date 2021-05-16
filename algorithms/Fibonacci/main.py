from config import limits


class Fibonacci:
    def __init__(self, n):
        self.n = int(n[0])

    def iter(self):
        a = 0
        b = 1
        if self.n < 0 or self.n > limits["fibonacci"]:
            return str(0)
        elif self.n == 0:
            return str(a)
        elif self.n == 1:
            return str(b)
        else:
            for i in range(2, self.n + 1):
                c = a + b
                a = b
                b = c
            return str(b)

    def get(self):
        return self.iter()
