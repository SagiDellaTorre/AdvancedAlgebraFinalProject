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
            raise Exception(f"a must be element in the prime field, where p={l.p}")

        self.l       = l                                       # The galois field object
        self.a_poly  = galois.Poly(a[::-1], field=self.l.GFP)  # a as a galois poly' object
        self.a_coeff = a                                       # list of the coeff' for a. Note the order!
        self.n_coeff = len(a)                                  # number of coeff'
        self.n_poly  = self.n_coeff - 1                        # The poly' degree

        # Varify the degree of the given poly' should be exactly [degree(fx)-1]
        if not self.n_poly == self.l.n_poly_fx - 1:
            raise Exception("The degree of the polynomial illegal in the corresponding field extension l") 

        self.a_mat = self.mat_represent()

    def __str__(self):
        """
        return instance as polynomials
        """
        return f"{self.a_poly}"

    def get_matrix(self):
        """
        return instance as matrix
        """
        return f"{self.a_mat}"

    def get_vector(self):
        """
        return instance as vector: for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
        """
        return f"{self.a_coeff}"

    def mat_represent(self):
        """
        this method calculate the matrix representation of an instance.
        The Finite field object holds a basis list of matrices.

        The total poly' matrix representation is than given by:
            for a poly: a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
            ---------
            a_mat = a_0*basis[0] + a_1*basis[1] + ... + a_n*basis[n]
            where basis[i] is a matrix!
            --------
        """
        mat = self.l.GFP(np.zeros((self.n_coeff, self.n_coeff), dtype=int))
        for i in range(self.n_coeff): # TODO: varify
            # mat = mat + self.a_poly.coeffs[-i-1]*self.l.basis[i]  # original, didn't work for case with a_n=0
            mat = mat + self.a_coeff[i] * self.l.basis[i]  # Amit: i think it is better to use the a_coeff list

        return mat
    
    def mat_to_poly(self, a_mat):  # TODO continue
        """
        this method translate from matrix representation to vector representation
        """
        pass

    def galois_poly_to_element(self, poly):
        return_coeff = self.l.zeros_pad_array(poly.coeffs)
        return_FiniteFieldElement = FiniteFieldElement(l=self.l, a=return_coeff[::-1])
        return return_FiniteFieldElement

    # adding two objects  
    def __add__(self, other):
        return_poly     = self.a_poly + other.a_poly
        return_FiniteFieldElement = self.galois_poly_to_element(return_poly)
        return return_FiniteFieldElement
    
    # subtract two objects
    def __sub__(self, other):
        return_poly = self.a_poly - other.a_poly
        return_FiniteFieldElement = self.galois_poly_to_element(return_poly)
        return return_FiniteFieldElement
    
    # multiply two objects 
    def __mul__(self, other):
        # multiply poly, and then modulo fx. all are galois poly object
        return_poly = (self.a_poly * other.a_poly) % self.l.fx_poly
        return_FiniteFieldElement = self.galois_poly_to_element(return_poly)
        return return_FiniteFieldElement
    
    # divide two objects
    def __truediv__(self, other):
        if all(num == 0 for num in other.a_coeff):
            raise Exception("Dividing by zero is not allowed")

        # option 1 (Amit): # TODO: still doesn't work correctly
        """
        for (a/b):
        We are using galois poly % operation to get the modulo of the division
        After the % operation, we should varify the result poly' is indeed in the field.

        for 2 given poly in the field, the division can't be greate degree of f(x), 
        so we dont need to use:   () % self.l.fx_poly
        """
        # return_poly = (self.a_poly % other.a_poly)  # TODO: not sure if % or //
        return_poly = (self.a_poly // other.a_poly)   # TODO: not sure if % or //
        return_FiniteFieldElement = self.galois_poly_to_element(return_poly)
        return return_FiniteFieldElement

        # option 1 (original by Sagi): Amit: why using self.a_mat? and not self.a_poly?
        # return (self.a_mat // other.a_poly) % self.l.fx_poly

        # #option 2:
        # c_mat = self.a_mat @ np.linalg.inv(other.a_mat)
        # return self.mat_to_poly(c_mat)



if __name__ == '__main__':
    pass