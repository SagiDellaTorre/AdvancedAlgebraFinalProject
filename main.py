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
    print(f"====================================")
    print(f"section (4) - matrix representation")
    print(f"====================================")

    p        = 47          # prime number to set the field
    fx_coeff = [42,3,0,1]  # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object
    a = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element

    print(f"polynomial a in matrix representation:\n{a.a_mat}")  # [[1,  2,  3], [15, 39,  2], [10,  9, 39]]

def run_section_5():
    #########################################
    # section (5) - basic operation for FiniteFieldElement
    #########################################
    print(f"====================================")
    print(f"section (5) - basic operation for FiniteFieldElement")
    print(f"====================================")

    p        = 47          # prime number to set the field
    fx_coeff = [42,3,0,1]  # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object
    a = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element
    b = FiniteFieldElement(l, [2, 3, 4])  # an object of finite field element

    print(f"l = \n{l}") # the FiniteField
    print(f"a = \n{a}") # FiniteFieldElement as a polynomial
    print(f"a = \n{a.get_matrix()}") # FiniteFieldElement as a matrix
    print(f"a = \n{a.get_vector()}") # FiniteFieldElement as a vector
    print(f"b = \n{b}") # FiniteFieldElement
    print("\nbasic operators:")
    print(f"a + b =\n{a + b}")  # 7x^2 + 5x + 3
    print(f"a - b =\n{a - b}")  # 46x^2 + 46x + 46
    print(f"a * b =\n{a * b}")  # 27x^2 + 16x + 40
    print(f"a / b =\n{a / b}")  # 36 #TODO verify and raise exeption if devide by 0
    
def main():
    # run_section_2()
    # run_section_4()
    run_section_5()


if __name__ == '__main__':
    main()