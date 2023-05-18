from PrimeFieldElement import PrimeFieldElement
from FiniteField import FiniteField
from FiniteFieldElement import FiniteFieldElement
import galois
import numpy as np


def run_section_2():
    #########################################
    # section (2) - basic operators
    #########################################
    print(f"=============")
    print(f"section (2) - basic operators")
    print(f"=============")

    a = PrimeFieldElement(3, 7)
    b = PrimeFieldElement(5, 7)
    # c = PrimeFieldElement(-1, 7)  # TODO: check it can't be in field

    print(f"a + b = {a + b}")  # 1
    print(f"a - b = {a - b}")  # 5
    print(f"a * b = {a * b}")  # 1
    print(f"a / b = {a / b}")  # 2
    print(f"a / a = {a / a}")  # 1
    print(f"inverse of a: {a.inverse()}")  # 5
    print(f"inverse of b: {b.inverse()}")  # 3

    # c = a.inverse()
    # print(f"a * a.inverse: {a*c}")  # 1  # TODO: ERROR: doesn't work because c is int and not a PrimeFieldElement object

    # matrix operation
    print(f"==== matrix operation =====")
    GF7 = galois.GF(7)
    a = GF7([[1, 2], [3, 4]])
    b = GF7([[3, 4], [5, 6]])

    print(f"a = \n{a}")
    print(f"b = \n{b}")
    print(f"a + b =\n{a + b}")  # [[4 6] [1 3]]
    print(f"a - b =\n{a - b}")  # [[5 5] [5 5]]
    print(f"a * b =\n{a * b}")  # [[3 1] [1 3]]   # * - element wise multipication
    print(f"a / b =\n{a / b}")  # [[5 4] [2 3]]   # / - element wise multipication
    print(f"a @ b =\n{a @ b}")  # [[6 2] [1 1]]   # @ - matrix multipication
    print(f"invers of a:\n{np.linalg.inv(a)}")  # [[5 1] [5 3]]
    print(f"invers of b:\n{np.linalg.inv(b)}")  # [[4 2] [6 2]]  # matrix inversion
    print(f"a @ inv(a) =\n{a @ np.linalg.inv(a)}")  # [[1 0] [0 1]] Identity matrix


def run_section_4():
    #########################################
    # section (4) - matrix representation
    #########################################
    print(f"===================================")
    print(f"section (4) - matrix representation")
    print(f"====================================")

    p        = 47          # prime number to set the field
    fx_coeff = [42,3,0,1]  # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object
    a = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element

    print(f"polynomial a in matrix representation:\n{a.a_mat}")  # [[1,  2,  3], [15, 39,  2], [10,  9, 39]]


def main():
    # run_section_2()
    run_section_4()


if __name__ == '__main__':
    main()