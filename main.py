import galois
import numpy as np

from PrimeFieldElement import PrimeFieldElement
from FiniteField import FiniteField
from FiniteFieldElement import FiniteFieldElement

def BSCS(l, g, y):
    """
    This method get a finite field, generator and a object y=g^x
    We want to solve the Discrete logarithm problem - to find x.

    :param l: Finite Field
    :param g: a generator in the finite field
    :param y: y = g^x
    :return:  x
    """
    q = l.p ** l.n_poly_fx - 1      # order of the finite field
    t = int(np.floor(np.sqrt(q)))
    big_step_list = []

    # Save all g^i for i=0,t,2t,3t,...
    for i in range(int(np.floor(q/t))+1):
        gi = g**(i*t)
        big_step_list.append(gi)


    for i in range(t+1):
        # Calc yi = y*g^i
        yi = y * (g**i)

        # find the index 'k' of the element in {g^i} so that yi=g^kt
        k = big_step_list.index(yi) if yi in big_step_list else -1
        if k >= 0:  # found!
            break

    # y*g^i=g^(kt)  ->  y=g^(kt-i)  ->  g^x=g^(kt-i)  -> x=(kt-i) mod q
    x = (k*t - i) % q
    return x


def run_section_2():
    print(f"=============================")
    print(f"section (2) - basic operators")
    print(f"=============================")

    a = PrimeFieldElement(3, 7)
    b = PrimeFieldElement(5, 7)
    # c = PrimeFieldElement(-1, 7) # Error

    print(f"a + b = {a + b}")  # 1
    print(f"a - b = {a - b}")  # 5
    print(f"a * b = {a * b}")  # 1
    print(f"a / b = {a / b}")  # 2
    print(f"a / a = {a / a}")  # 1
    print(f"inverse of a: {a.inverse()}")  # 5
    print(f"inverse of b: {b.inverse()}")  # 3

    c = a.inverse()
    print(f"a * a.inverse: {a*c}")  # 1

    # matrix operation, using galois operations
    print(f"\n==== matrix operation =====")
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
    print(f"inverse of a:\n{np.linalg.inv(a)}")  # [[5 1] [5 3]]
    print(f"inverse of b:\n{np.linalg.inv(b)}")  # [[4 2] [6 2]]  # matrix inversion
    print(f"a @ inv(a) =\n{a @ np.linalg.inv(a)}")  # [[1 0] [0 1]] Identity matrix


def run_section_3():
    print(f"====================================")
    print(f"section (3) - Finite Field")
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
    print(f"section (4) - finite field element and matrix representation")
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

    # # Test Exception
    # print("Test Exception - divide by zero")
    # c = FiniteFieldElement(l, [0, 0, 0])  # an object of finite field element
    # print(f"c as poly': \n{c}")  # FiniteFieldElement as a polynomial
    # ac_div = a / c
    # print(f"a / c =\n{ac_div}")


def run_section_6():
    """
    The input is a poly' and an int number
    The output should be the poly^n
    :return:
    """
    print(f"=============================")
    print(f"section (6) - exponentiation")
    print(f"=============================")

    # Define a Finite Field
    p        = 47                 # prime number to set the field
    fx_coeff = [42, 3, 0, 1]      # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define 2 poly in the field:
    # # Test case 1:
    a = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element
    I = a/a       # identity element

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
    print(f"=============================")
    print(f"section (7) - find order")
    print(f"=============================")

    # Define a Finite Field
    p        = 47                 # prime number to set the field
    fx_coeff = [42, 3, 0, 1]      # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    a    = FiniteFieldElement(l, [1, 2, 3])  # an object of finite field element
    I    = a/a
    zero = a-a  # To be used later (for test error)

    # --- Pretty-print of the Field and some element in the field ---
    print(f"l = \n{l}")  # the FiniteField

    print(f"a as poly':    \n{a}")  # FiniteFieldElement as a polynomial
    print(f"a as matrix:   \n{a.get_matrix()}")  # FiniteFieldElement as a matrix
    print(f"a as a vector: \n{a.get_vector()}\n")  # FiniteFieldElement as a vector

    order, gen_list = a.order()
    print(f"order of a is: {order}")

    order, gen_list = I.order()
    print(f"order of I is: {order}")

    # order, gen_list = zero.order()
    # print(f"order zero={order}")


def run_section_8():
    """
    (8) Implement a method for FiniteField that finds a generator 'g' of the multiplicative which we know is cyclic.

    Find a generator g: we need to find element in l^x so that for each a in l^x we can write
                            a = g^n, for some int n

    :return:
    """
    print(f"=============================")
    print(f"section (8) - find generator")
    print(f"=============================")

    # Example 1
    print("\nExample 1")
    # Define a Finite Field - in this case it is like a !prime field!
    p        = 5                  # prime number to set the field
    fx_coeff = [0, 1]             # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    g = l.generator()
 
    print(f"generator of the finite field {l} is:\n{g}")  # The generator is x

    # Example 2
    print("\nExample 2")
    # Define a Finite Field
    p        = 5                  # prime number to set the field
    fx_coeff = [2, 4, 1]          # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    g = l.generator()
 
    print(f"generator of the finite field {l} is:\n{g}")  # The generator is x

    # Example 3
    print("\nExample 3")
    # Define a Finite Field
    p        = 47                 # prime number to set the field
    fx_coeff = [42, 3, 0, 1]      # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    g = l.generator()
 
    print(f"generator of the finite field {l} is:\n{g}")  # The generator is 5x^2


def run_section_9():
    """
    Using the BSGS algorithm, write a function to solve the discrete logarithm problem.
    That is, given g^t in l^x, find the natural number 1<= t <p^n
    """
    print(f"=============================")
    print(f"section (9) - BSCS")
    print(f"=============================")

    # Example 1
    print("\nExample 1")
    # Define a Finite Field
    p        = 29                 # prime number to set the field
    fx_coeff = [0, 1]             # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    g = l.generator()
    x = 21
    y = g**x # an object of finite field element
    print(f"generator of the finite field {l} is: {g}") # The generator is g
    print(f"x = {x}")
    print(f"y = g^x as poly': {y}")
    print(f"we should find x")

    # find x where y = g^x (in our case x = 8)
    x_bscs = BSCS(l, g, y)
 
    print(f"x from BSCS = {x_bscs}")
    print(f"indeed: {y} = ({g})^{x} = {g**x_bscs}")
    
    # Example 2
    print("\nExample 2")
    # Define a Finite Field
    p        = 3             # prime number to set the field
    fx_coeff = [1, 2, 0, 1]  # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    g = l.generator()
    x = 6  # 6 , -1
    y = g**x # an object of finite field element
    print(f"generator of the finite field {l} is: {g}") # The generator is g
    print(f"x = {x}")
    print(f"y = g^x as poly': {y}")
    print(f"we should find x")

    # find x where y = g^x (in our case x = 8)
    x_bscs = BSCS(l, g, y)
 
    print(f"x from BSCS = {x_bscs}")
    print(f"indeed: {y} = ({g})^{x} = {g**x_bscs}")
    
    # Example 3
    print("\nExample 3")
    # Define a Finite Field
    p = 47                        # prime number to set the field
    fx_coeff = [42, 3, 0, 1]      # a irreducible poly' coeff': for a_n*x^n+...+a_1*x+a_0 -> [a_0, a_1, ...]
    l = FiniteField(p, fx_coeff)  # the finite field object

    # Define poly in the field:
    g = l.generator()
    x = 163
    y = g**x # an object of finite field element
    print(f"generator of the finite field {l} is: {g}") # The generator is g
    print(f"x = {x}")
    print(f"y = g^x as poly': {y}")
    print(f"we should find x")

    # find x where y = g^x (in our case x = 8)
    x_bscs = BSCS(l, g, y)
 
    print(f"x from BSCS is: {x_bscs}")
    print(f"indeed: {y} = ({g})^{x} = {g**x_bscs}")

def main():
    # run_section_2()
    # run_section_3()
    # run_section_4()
    # run_section_5()
    # run_section_6()
    # run_section_7()
    # run_section_8()
    run_section_9()
    pass


if __name__ == '__main__':
    """
    Code written by 
    Sagi Della Torre ID: 205780836
    Amit Eliav, ID: 204053466
    
    To run the code you should have the imported packages
    and uncomment the run_section_i for each of the sections
    """
    main()