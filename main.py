from PrimeFieldElement import PrimeFieldElement
from FiniteField import FiniteField
from FiniteFieldElement import FiniteFieldElement

def main():
    """
    This function test the different section of the code, but the 'Directions' given to us
    """
    #########################################
    # section (2) - basic operators
    #########################################
    a = PrimeFieldElement(a=3, p=7)
    b = PrimeFieldElement(a=5, p=7)
    c = PrimeFieldElement(a=6, p=7)

    print(f"a, b, c are: {a},{b}, {c}")
    print(f"a + b = {a + b}")
    print(f"a + c = {a + c}")
    print(f"a - b = {a-b}")
    print(f"a - c = {a - c}")
    print(f"a * b = {a*b}")
    print(f"a / b = {a/b}")
    print(f"a / c = {a / c}")
    print(f"inverse of a: {a.inverse()}")
    print(f"inverse of b: {b.inverse()}")
    print(f"inverse of c: {c.inverse()}")
    # ==========================================




if __name__ == '__main__':
    main()