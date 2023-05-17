import galois
import numpy as np

class FiniteField:
    """
    see section (3) in the pdf
    This class represents 'l':
              l ∼=k[x]/⟨f(x)⟩
    """
    # constructor
    def __init__(self, p, fx):
        """

        :param p:  a prime number
        :param fx: a list of polynomial's coefficients.
                   given in common printed form a_n * x^n + ... + a_1 * x + a_0
                   and as a list of coefficients [a_0, a_1, ...]. Note the order.
        """
        self.p = p      # assume that p is indeed prime
        self.fx = fx    # assume that fx is indeed irreducible

        # make the poly' a Monic polynomial (so a_n=1)
        # TODO: the coefficients should be in F. do we make use they are?
        self.fx = (np.array(self.fx) / self.fx[-1]).tolist()