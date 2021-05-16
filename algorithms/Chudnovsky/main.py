from math import log10
from gmpy2 import mpz, isqrt
from config import limits


class Chudnovsky:
    A = 13591409
    B = 545140134
    C = 640320
    D = 426880
    E = 10005
    C3_24 = C ** 3 // 24
    DIGITS_PER_TERM = log10(C3_24 / 6 / 2 / 6)  # => 14.181647462725476

    def __init__(self, digits):
        """ Initialization
        :param int digits: digits of PI computation
        """
        self.digits = int(digits[0])
        self.n = int(self.digits / self.DIGITS_PER_TERM + 1)

    def compute(self):
        """ Computation """

        if self.digits > limits['chudnovsky']:
            return str(0)

        p, q, t = self.__bsa(0, self.n)
        one_sq = mpz(10) ** (2 * self.digits)
        sqrt_c = isqrt(self.E * one_sq)
        return str((q * self.D * sqrt_c) // t)

    def __bsa(self, a, b):
        """ PQT computation by BSA(= Binary Splitting Algorithm)
        :param int a: positive integer
        :param int b: positive integer
        :return list [int p_ab, int q_ab, int t_ab]
        """
        if a + 1 == b:
            if a == 0:
                p_ab = q_ab = 1
            else:
                p_ab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                q_ab = mpz(a * a * a * self.C3_24)
            t_ab = p_ab * (self.A + self.B * a)
            if a & 1:
                t_ab *= -1
        else:
            m = (a + b) // 2
            p_am, q_am, t_am = self.__bsa(a, m)
            p_mb, q_mb, t_mb = self.__bsa(m, b)
            p_ab = p_am * p_mb
            q_ab = q_am * q_mb
            t_ab = q_mb * t_am + p_am * t_mb
        return [p_ab, q_ab, t_ab]

    def get(self):
        return self.compute()
