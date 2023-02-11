import numpy as np

# representing polynomial 
# ax^n + bx^(n-1) + cx^(n-2) becomes [c, b, a]
# navie evaluation  --> O(n^n)
# horner's rule evalution --> O(n)

# helper functions
def printPolynomial(coefficients):
    currDeg = int(coefficients.size-1)        
    print("The polynomial expression is --> ", end="")
    for _ in range(coefficients.size-2):
        print("{}(x^{}) + ".format(coefficients[currDeg], currDeg), end="")
        currDeg -= 1
    print("{}(x) + ".format(coefficients[1]), end="")
    print("{}\n".format(coefficients[0]))


def power_of_n(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res


def polynomialExpr(coefficients, x_var):
    x_var = float(x_var)
    currDeg = int(coefficients.size-1)
    resStr = ""
    for _ in range(coefficients.size-2):
        resStr += "{}({}) + ".format(coefficients[currDeg], power_of_n(x_var, currDeg))
        currDeg -= 1
    resStr += "{}({}) + ".format(coefficients[1], x_var)
    resStr += "{}".format(coefficients[0])
    return resStr


def evaluatePolynomial_navie(coeffs, x):
    res = 0
    for deg, coeff in enumerate(coeffs):
        res += coeff * power_of_n(x, int(deg))
    return res


def evaluatePolynomial_horner(coeffs, x):
    # ax^3+bx^2+cx+d = ((ax+b)*x+c)*x+d 
    # where first iteration is ax+b, second is (...)*x+c
    currDeg = int(coeffs.size-1)
    res = coeffs[currDeg]
    for _ in range(coeffs.size-1):
        currDeg -= 1
        res = res*x + coeffs[currDeg]
    return res

##################################################################
# getting polynomial from command line        
deg = int(input("degree of the polynomial: "))
polynomial_coefficients = np.zeros(deg + 1)
for i in range(polynomial_coefficients.size):
    polynomial_coefficients[i] = input("enter coefficient for degree {}: ".format(i))

printPolynomial(polynomial_coefficients)

x_val = float(input("evaluate above expression at x="))
EvalStr = polynomialExpr(polynomial_coefficients, x_val)
print("{} = {}".format(EvalStr, evaluatePolynomial_navie(polynomial_coefficients, x_val)))
print("{} = {}".format(EvalStr, evaluatePolynomial_horner(polynomial_coefficients, x_val)))
