import galois
import numpy as np
import itertools
from FiniteFieldElement import FiniteFieldElement

class FiniteField:
    # constructor
    def __init__(self, p, fx):
        """
        define a Finite Field element.
        :param p:  a prime number to set the field
        :param fx: an irreducible polynom coefficients. a_n * x^n + ... + a_1 * x + a_0
                   so the fx list is [a_0, a_1, ...]
        """
        self.p         = p                                       # a prime number
        self.GFP       = galois.GF(p)                            # the galois field
        self.fx_coeff  = fx                                      # the poly coefficients
        self.fx_poly   =  galois.Poly(fx[::-1], field=self.GFP)  # a galois object for the fx polynom
        self.n_poly_fx = len(fx)-1                               # the degree of fx, as int number
        self.basis     = self.set_basis()                        # list, holding a basis matrices

        self.varify_irreducible()

    def varify_irreducible(self):
        """
        we should check that the poly is indeed irreducible for degrees 2-3,
        we can do that by checking all the possible options.
        for example,for F_7, and poly x^2+2x+1. we should do:
            for i in range(0,7):
                i^2+2i+1 = 0 ?
            if all are not.. it is irreducible
        """
        if self.n_poly_fx == 2 or self.n_poly_fx == 3:
            for i in range(0, self.p):
                if self.fx_poly(i) == 0:
                    raise Exception(f"Poly' f(x) must be irreducible!. x={i} is a root value of f(x)")

    # for print function
    def __str__(self):
        return f"F[{self.p}]({self.fx_poly})"

    def set_basis(self):
        """
        This method create a basis matrices list.
        For example: for GL3[k] the basis will be of len 3, with 3 matrices of shape 3x3.
        :return: the basis
        """
        basis = []
        for i in range(self.n_poly_fx):
            # append a zero galois matrix, later to be filled with the basis[i]
            basis.append(self.GFP(np.zeros((self.n_poly_fx,self.n_poly_fx), dtype=int)))

            # Create a one-hot-encoding vector
            vac1 = [1 if x == i else 0 for x in range(self.n_poly_fx)]

            for j in range(self.n_poly_fx):
                vec2 = [1 if x == j else 0 for x in range(self.n_poly_fx)]
                poly_mul = self.poly_mul(vac1, vec2)  # find the [Tg]_B transformation
                # insert the vector value in reverse order (to match between our convention and galois)
                for k in range(len(poly_mul)):
                    basis[i][j,k] = poly_mul[-k-1]  # test case: x^1 * (x^2 + x + 1)

        return basis
    
    def poly_mul(self, a, b):
        """
        This method takes 2 poly' a and b and multiply them.
        the return value is the residual poly in the Finite Field.
        :param a: poly coeff' of max degree < degree(fx)
        :param b: poly coeff' of max degree < degree(fx)
        :return: the residual poly coeff' in the field, i.e degree<degree(fx)
        """
        a = galois.Poly(a[::-1], field=self.GFP)
        b = galois.Poly(b[::-1], field=self.GFP)
        c = a * b
        c_res = c % self.fx_poly  # this is a galois poly' operation! return a poly' object!

        return self.zeros_pad_array(c_res.coeffs)

    def zeros_pad_array(self, a):
        """
        take a galois poly' object coeff' list, and return list padded with zeros
        since galois poly' coeff' list for a=1 is [1], but we want it to be in the len of the ply
        i.e: in a field where the poly' are at max degree of 3: [1,0,0,0]
        :param a: galois poly' coeff' list
        :return:
        """
        return self.GFP(np.pad(a, (self.n_poly_fx-len(a), 0)))

    def generator(self):
        coeff_list = range(self.p)
        element_iter = itertools.product(coeff_list, repeat=self.n_poly_fx)  # all the combination with replacment and order matters
        elements_generated_list = []

        for element in element_iter:  # loop over all the elements in the finite field and check which one of them is the generator
            if all(num == 0 for num in element): # jump over zero element
                continue
            
            FiniteFieldEle = FiniteFieldElement(l=self, a=element)
            if FiniteFieldEle in elements_generated_list:  # jump over elements from the empty list (elements we already generated)
                continue

            order, curr_elements_genereted_list = FiniteFieldEle.order()  # get the order of the current element
            elements_generated_list = elements_generated_list + curr_elements_genereted_list # add to the list all the elements which generate from the current element
            if order == self.p ** self.n_poly_fx - 1: # only generator has this order - generate all the elements in the field except for zero
                generator = FiniteFieldEle
                break

        return generator


if __name__ == '__main__':
    pass