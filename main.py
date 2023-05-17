from PrimeFieldElement import PrimeFieldElement
from FiniteField import FiniteField
from FiniteFieldElement import FiniteFieldElement
import galois
import numpy as np

def main():

    #########################################
    # section (2) - basic opertors
    #########################################

    a = PrimeFieldElement(3,7)
    b = PrimeFieldElement(5,7)

    print("a + b = {}".format(a+b)) #1
    print("a - b = {}".format(a-b)) #5
    print("a * b = {}".format(a*b)) #1
    print("a / b = {}".format(a/b)) #2
    print("invers of a: {}".format(a.inverse())) #5
    print("invers of b: {}".format(b.inverse())) #3

    # matrix operation
    GF7 = galois.GF(7)
    a = GF7([[1,2],[3,4]])
    b = GF7([[3,4],[5,6]])

    print("a = {}".format(a))
    print(f"b = {b}")
    print("a + b = {}".format(a+b)) #[[4 6] [1 3]]
    print("a - b = {}".format(a-b)) #[[5 5] [5 5]]
    print("a * b = {}".format(a*b)) #[[3 1] [1 3]] # * - element wise multipication
    print("a / b = {}".format(a/b)) #[[5 4] [2 3]] # / - element wise multipication
    print("a @ b = {}".format(a@b)) #[[6 2] [1 1]]  # @ - matrix multipication
    print("invers of a: {}".format(np.linalg.inv(a))) #[[5 1] [5 3]]
    print("invers of b: {}".format(np.linalg.inv(b))) #[[4 2] [6 2]] #matrix inversion
    print("a @ inv(a) = {}".format(a @ np.linalg.inv(a))) #[[1 0] [0 1]]

    #########################################
    # section (4) - matrix representation
    #########################################

    l = FiniteField(47,[42,3,0,1])
    a = FiniteFieldElement(l, [1, 2, 3])

    print("polynomial a in matrix representation: {}".format(a.a_mat)) # [[1,  2,  3], [15, 39,  2], [10,  9, 39]]

if __name__ == '__main__':

    main()