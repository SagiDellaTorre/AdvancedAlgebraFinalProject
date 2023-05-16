from PrimeFieldElement import PrimeFieldElement
from FiniteField import FiniteField
from FiniteFieldElement import FiniteFieldElement

def main():

    #########################################
    # section (2) - basic opertors
    #########################################

    a = PrimeFieldElement(3,7)
    b = PrimeFieldElement(5,7)

    print("a + b = {}".format(a+b))
    print("a - b = {}".format(a-b))
    print("a * b = {}".format(a*b))
    print("a / b = {}".format(a/b))
    print("invers of a: {}".format(a.inverse()))
    print("invers of b: {}".format(b.inverse()))

if __name__ == '__main__':
    main()