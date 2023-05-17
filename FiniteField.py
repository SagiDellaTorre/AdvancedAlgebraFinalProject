import galois

class FiniteField:
    """
    see section (3) in the pdf
    This class represents 'l':
              l ∼=k[x]/⟨f(x)⟩
    """
    # constructor
    def __init__(self, p, fx):
        self.p = p      # assume that p is indeed prime
        self.fx = fx    # assume that fx is indeed irreducible
