from PrimeFieldElement import PrimeFieldElement
from FiniteField import FiniteField
from FiniteFieldElement import FiniteFieldElement
import galois
import numpy as np


def run_section_2():
    print(f"=============================")
    print(f"section (2) - basic operators")
    print(f"=============================")

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


def run_section_3():
    print(f"====================================")
    print(f"section (3) - matrix representation")
    print(f"====================================")
    # Define a Finite Field:
    p        = 7                  # prime number to set the field
    fx_coeff = [1, 0, 1]          # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object
    print(f"finite field l is:\n{l}")

    # # Example for setting the field with a !reducible! poly
    # p        = 7                  # prime number to set the field
    # fx_coeff = [1, 2, 1]          # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    # l = FiniteField(p, fx_coeff)  # the finite field object
    # print(f"finite field l is:\n{l}")


def run_section_4():
    print(f"====================================")
    print(f"section (4) - matrix representation")
    print(f"====================================")

    # Define a Finite Field:
    p        = 47                 # prime number to set the field
    fx_coeff = [42, 3, 0, 1]      # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define a poly' by its coeff'
    a_coeff = [1, 2, 3]
    b_coeff = [1, 1, 1]
    a = FiniteFieldElement(l, a_coeff)  # an object of finite field element
    b = FiniteFieldElement(l, b_coeff)  # an object of finite field element

    print(f"polynomial a coeff' are:\n{a_coeff}")
    print(f"polynomial a in matrix representation:\n{a.a_mat}\n")  # [[1, 2, 3], [15, 39, 2], [10, 9, 39]]

    print(f"polynomial b coeff' are:\n{b_coeff}")
    print(f"polynomial b in matrix representation:\n{b.a_mat}")  # [[1, 1, 1], [5, 45  1], [5, 2, 45]]


def run_section_5():
    """
    In this section show:
    (1) pretty-print
    (2) basic matrix operations:
        2.1 add
        2.1 sub
        2.3 mul
        2.3 truediv
    ** Remember to raise an exception when dividing by zero.
    """
    print(f"====================================================")
    print(f"section (5) - basic operation for FiniteFieldElement")
    print(f"====================================================")

    # Define a Finite Field
    p        = 47                 # prime number to set the field
    fx_coeff = [42, 3, 0, 1]      # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define 2 poly in the field:
    # # Test case 1:
    a = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element
    b = FiniteFieldElement(l, [2, 3, 4])  # an object of finite field element

    # Test case 2:
    # a = FiniteFieldElement(l, [1, 0, 3])   # an object of finite field element
    # b = FiniteFieldElement(l, [3, 5, 45])  # an object of finite field element

    # --- Pretty-print of the Field and some element in the field ---
    print(f"l = \n{l}")                          # the FiniteField
    print(f"a as poly':    \n{a}")               # FiniteFieldElement as a polynomial
    print(f"a as matrix:   \n{a.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"a as a vector: \n{a.get_vector()}")  # FiniteFieldElement as a vector

    print(f"b as poly':    \n{b}")                 # FiniteFieldElement as a polynomial
    print(f"b as matrix:   \n{b.get_matrix()}")    # FiniteFieldElement as a matrix
    print(f"b as a vector: \n{b.get_vector()}\n")  # FiniteFieldElement as a vector
    # ---------------------------------------

    # --- Basic operation in the finite field ---
    print("---basic operators in the finite field: ---")
    # Sum:
    ab_sum = a+b
    print(f"a + b =\n{ab_sum}")  # 7x^2 + 5x + 3
    print(f"a + b as matrix: \n{ab_sum.get_matrix()}\n")

    # sub
    ab_sub = a - b
    print(f"a - b =\n{ab_sub}")  # 46x^2 + 46x + 46
    print(f"a - b as matrix: \n{ab_sub.get_matrix()}\n")

    # mul
    ab_mul = a * b
    print(f"a * b =\n{ab_mul}")  # 27x^2 + 16x + 40
    print(f"a * b as matrix: \n{ab_mul.get_matrix()}\n")

    # div
    aa_div = a / a
    print(f"a / a =\n{aa_div}")  # should be 1
    print(f"a / a as matrix: \n{aa_div.get_matrix()}\n")

    ab_div = a / b
    print(f"a / b =\n{ab_div}")  #
    print(f"a / b as matrix: \n{ab_div.get_matrix()}\n")

    # Test Exception
    print("Test Exception - divide by zero")
    c = FiniteFieldElement(l, [0, 0, 0])  # an object of finite field element
    print(f"c as poly': \n{c}")  # FiniteFieldElement as a polynomial
    ac_div = a / c
    print(f"a / c =\n{ac_div}")


def run_section_6():
    """
    The input is a poly' and an int number
    The output should be the poly^n
    :return:
    """
    # Define a Finite Field
    p = 47  # prime number to set the field
    fx_coeff = [42, 3, 0, 1]  # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define 2 poly in the field:
    # # Test case 1:
    a = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element
    I = a/a  #

    b = a ** 0
    c = a ** 1
    d = a ** 2
    e = a ** 3
    f = a ** -1
    g = a ** -2
    h = a ** -4

    # --- Pretty-print of the Field and some element in the field ---
    print(f"l = \n{l}")  # the FiniteField
    print(f"a as poly':    \n{a}")  # FiniteFieldElement as a polynomial
    print(f"a as matrix:   \n{a.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"a as a vector: \n{a.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"b as poly':    \n{b}")  # FiniteFieldElement as a polynomial
    print(f"b as matrix:   \n{b.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"b as a vector: \n{b.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"c as poly':    \n{c}")  # FiniteFieldElement as a polynomial
    print(f"c as matrix:   \n{c.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"c as a vector: \n{c.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"d as poly':    \n{d}")  # FiniteFieldElement as a polynomial
    print(f"d as matrix:   \n{d.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"d as a vector: \n{d.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"e as poly':    \n{e}")  # FiniteFieldElement as a polynomial
    print(f"e as matrix:   \n{e.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"e as a vector: \n{e.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"f as poly':    \n{f}")  # FiniteFieldElement as a polynomial
    print(f"f as matrix:   \n{f.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"f as a vector: \n{f.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"g as poly':    \n{g}")  # FiniteFieldElement as a polynomial
    print(f"g as matrix:   \n{g.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"g as a vector: \n{g.get_vector()}\n")  # FiniteFieldElement as a vector

    print(f"h as poly':    \n{h}")  # FiniteFieldElement as a polynomial
    print(f"h as matrix:   \n{h.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"h as a vector: \n{h.get_vector()}\n")  # FiniteFieldElement as a vector

    a_inv = I / a  # We can see a**-1 = a_inv
    print(f"a_inv as poly':    \n{a_inv}")  # FiniteFieldElement as a polynomial
    print(f"a_inv as matrix:   \n{a_inv.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"a_inv as a vector: \n{a_inv.get_vector()}\n")  # FiniteFieldElement as a vector


def run_section_7():
    """
    Input is: poly' a in 'l^x' (l without 0).
    return value is: the order of a. that means, how many times we need to multiply a*...*a to get 1 (identity)

    Because l^x is cyclic - there should be always a solution for this problem
    :return: order(a)
    """
    # Define a Finite Field
    p = 47  # prime number to set the field
    fx_coeff = [42, 3, 0, 1]  # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    a    = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element
    I    = a/a
    zero = a-a

    # --- Pretty-print of the Field and some element in the field ---
    print(f"l = \n{l}")  # the FiniteField

    print(f"a as poly':    \n{a}")  # FiniteFieldElement as a polynomial
    print(f"a as matrix:   \n{a.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"a as a vector: \n{a.get_vector()}\n")  # FiniteFieldElement as a vector

    order = a.order()
    print(f"order a={order}")

    order = I.order()
    print(f"order I={order}")

    # order = zero.order()
    # print(f"order zero={order}")


def run_section_8():
    """
    (8) Implement a method for FiniteField that finds a generator 'g' of the multiplicative which we know is cyclic.

    Find a generator g: we need to find element in l^x so that for each a in l^x we can write
                            a = g^n, for some int n

    :return:
    """
    pass

def run_section_9():
    """
    Using the BSGS algorithm, write a function to solve the discrete logarithm problem.
    That is, given g^t in l^x, find the natural number 1<=t<=p^n

    :return: 
    """
    
    pass

def main():
    # run_section_2()
    # run_section_3()
    # run_section_4()
    # run_section_5()
    # run_section_6()
    run_section_7()
    # run_section_8()
    # run_section_9()
    pass


if __name__ == '__main__':
    # TODO:
    """
    General TODO:
    1. (Done) 
        in section 3: we should check that the poly is indeed irreducible for degrees 2-3, 
        we can do that by checking all the possible options. 
        for example,for F_7, and poly x^2+2x+1. we should do:
            for i in range(0,7):
                i^2+2i+1 = 0 ?
            if all are not.. it is irreducible
    
    2. (Done)
        when operating with FiniteFieldElement, the return object is galois poly.
        than means, we can't use it anymore later as a FiniteFieldElement.
        should we return a
    3. XXX
        in PrimeFieldElement - in all operators - return a PrimeFieldElement object instead of int's values        
    """
    main()