import galois
import numpy as np

class FiniteField:

    # constructor
    def __init__(self, p, fx):

        self.p = p
        self.GFP = galois.GF(p)
        self.fx_coff = fx
        self.fx_poly =  galois.Poly(fx[::-1], field=self.GFP)
        self.n_poly_fx = len(fx)-1
        self.basis = self.set_basis()

    def set_basis(self):

        basis = []
        for i in range(self.n_poly_fx):

            basis.append(self.GFP(np.zeros((self.n_poly_fx,self.n_poly_fx), dtype=int)))
            arr = [1 if x == i else 0 for x in range(self.n_poly_fx)]

            for j in range(self.n_poly_fx):
                
                arr2 = [1 if x == j else 0 for x in range(self.n_poly_fx)]

                poly_mul = self.poly_mul(arr,arr2)
                for k in range(len(poly_mul)):

                    basis[i][j,k] = poly_mul[-k-1] # x^1 * (x^2 + x + 1)

        return basis
    
    def poly_mul(self, a, b):

        a = galois.Poly(a[::-1], field=self.GFP)
        b = galois.Poly(b[::-1], field=self.GFP)
        new_array = a * b
        new_array_reduced = new_array % self.fx_poly

        return self.zeros_padd_array(new_array_reduced.coeffs)
    
    def zeros_padd_array(self, a):

        return self.GFP(np.pad(a, (self.n_poly_fx-len(a),0)))
