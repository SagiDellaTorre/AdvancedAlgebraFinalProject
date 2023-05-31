import galois
import numpy as np
import itertools

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

        self.a_mat    = self.mat_represent()
        self.identity = self.l.GFP(np.identity(self.n_coeff, dtype=int))  # galois identity matrix

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
        for i in range(self.n_coeff):
            mat = mat + self.a_coeff[i] * self.l.basis[i]

        return mat

    def galois_poly_to_element(self, poly):
        return_coeff = self.l.zeros_pad_array(poly.coeffs)
        return_FiniteFieldElement = FiniteFieldElement(l=self.l, a=return_coeff[::-1])
        return return_FiniteFieldElement

    def __str__(self):
        """
        return instance as polynomials
        """
        return f"{self.a_poly}"

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
        """
        method for dividing 2 poly'. a/b
        self has the poly a, other has the poly b.
        we use matrix operation. a*(b^-1)
        the return poly is the rist row of the result matrix.

        Note: all poly's are in GL(), so they should all have a valid inverse matrix.
        :param other:  poly b
        :return: a/b as a FiniteFieldElement object
        """
        if all(num == 0 for num in other.a_coeff):
            raise Exception("Dividing by zero is not allowed")

        c_mat = self.a_mat @ np.linalg.inv(other.a_mat)
        return_FiniteFieldElement = FiniteFieldElement(l=self.l, a=c_mat[0, :])
        return return_FiniteFieldElement

    def __pow__(self, power, modulo=None):
        """
        using galois and numpy operators
        :param power:   int number
        :param modulo:
        :return: self to the power of 'power'
        """
        power_mat = np.linalg.matrix_power(self.a_mat, power)
        return_FiniteFieldElement = FiniteFieldElement(l=self.l, a=power_mat[0, :])
        return return_FiniteFieldElement

    def __eq__(self, other):
        
        if np.all(self.a_coeff == other.a_coeff):
            ret = True
        else:
            ret = False
        
        return ret
        
    def order(self):
        """
        check the order of element
        error for the zero element
        :return: order (int from 1 to p^n-1)
        :return: ist of all the elements which generated from the current element
        """
        if all(num == 0 for num in self.a_coeff):
            raise Exception("ERROR: order of zero is not defined")

        mul_mat = self.a_mat
        gen_list = [] # list of all the elements which generated from the current element
        order = 1
        while np.any(mul_mat != self.identity):
            mul_mat = mul_mat @ self.a_mat  # @ for matrix multiplication!
            order += 1
            gen_list.append(FiniteFieldElement(l=self.l, a=mul_mat[0, :])) # add all the element which generate from our element to a list
        return order, gen_list
    
if __name__ == '__main__':
    pass