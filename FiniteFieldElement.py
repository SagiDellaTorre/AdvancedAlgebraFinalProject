import galois

class FiniteFieldElement:
    """
    see section (3) in the pdf
    This class represents α ∈ l:
        an element α ∈ l can be given as [a0, a1, . . . , an−1] or as a0 + a1*x + · · · + a_(n−1)*x^(n−1)
        for some coefficients ai ∈ k

    In particular, the cardinality of l is p^n, and you can assume it is less than 2^32.
    """
    # constructor
    def __init__(self, a):
        self.a = a
        self.n = len(a)