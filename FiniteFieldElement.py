import galois
import numpy as np

class FiniteFieldElement:

    # constructor
    def __init__(self, l, a):
        """
        l : FiniteField 
        a : array of polynomial coefficients
        """

        if max(a) >= l.p or min(a) < 0:
            raise Exception(f"a must be element in the prime field p={l.p}")

        self.l = l
        self.a_poly = galois.Poly(a[::-1], field=self.l.GFP)
        self.a_coeff = a
        self.n_coeff = len(a)
        self.n_poly = self.n_coeff - 1

        if not self.n_poly == self.l.n_poly_fx - 1:
            raise Exception("The degree of the polynomial illegal in the corresponding field extension l") 

        self.a_mat = self.mat_represent()

    def mat_represent(self):

        mat = self.l.GFP(np.zeros((self.n_coeff,self.n_coeff), dtype=int))
        for i in range(self.n_coeff):
            mat = mat + self.a_poly.coeffs[-i-1]*self.l.basis[i]

        return mat