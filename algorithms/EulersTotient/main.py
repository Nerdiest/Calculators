class EulersTotient:
    def __init__(self, n):
        self.n = int(n[0])

    def gcd(self, x, y):
        while y:
            x,y = y,x % y
        return x

    def get(self):
        r = 0
        for i in range(1, self.n+1):
            if self.gcd(i, self.n) == 1:
                r += 1
        return str(r)

