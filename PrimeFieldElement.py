import galois

class PrimeFieldElement:

    # constructor
    def __init__(self, a, p):
        if a >= p or a < 0:
            raise Exception(f"a must be element in the prime field, where p={p}")

        self.GFP      = galois.GF(p)
        self.a        = self.GFP(a)   # TODO: check a can be in the field
        self.a_int    = a
        self.p_int    = p

    # for print function
    def __str__(self):
        return "{}".format(self.a)

    # adding two objects  
    def __add__(self, other):
        return PrimeFieldElement(self.a + other.a, self.p_int)
    
    # substract two objects  
    def __sub__(self, other):
        return PrimeFieldElement(self.a - other.a, self.p_int)
    
    # multiply two objects  
    def __mul__(self, other):
        return PrimeFieldElement(self.a * other.a, self.p_int)
    
    # find inverse of objects  
    def inverse(self):
        # find a_inv and t such that: a * a_inv + p * t = 1
        gcd, a_inv_int, t = galois.egcd(self.a_int, self.p_int)
        return PrimeFieldElement(a_inv_int % self.p_int,self.p_int)

    # adding two objects  
    def __truediv__(self, other):
        return self * other.inverse()


if __name__ == '__main__':
    pass