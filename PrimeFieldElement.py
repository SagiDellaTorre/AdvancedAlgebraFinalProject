import galois

class PrimeFieldElement:
    # constructor
    def __init__(self, a, p):
        self.GFP = galois.GF(p)
        self.a = self.GFP(a)
        self.a_int = a
        self.p_int = p

    # adding two objects  - overload for '+'
    def __add__(self, other):
        return self.a + other.a
    
    # subtract two objects - overload for '-'
    def __sub__(self, other):
        return self.a - other.a
    
    # multiply two objects - overload for '*'
    def __mul__(self, other):
        return self.a * other.a
    
    # find inverse of objects  
    def inverse(self):
        """
         gcd is 'greatest common divisor'
        """
        # find a_inv and t such that: a * a_inv + p * t = 1
        gcd, a_inv_int, t = galois.egcd(self.a_int, self.p_int)
        return a_inv_int % self.p_int

    # divide two objects - overload for '/'
    def __truediv__(self, other):
        return self.a * other.inverse()

