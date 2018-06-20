# find the Greatest Common Divisor of 2 integers

def euclidean_gcd (a, b):

    if a == 0: return b
    if b == 0: return a

    # dont trust user input
    # swap values if b is greater than a
    if b > a:
        b,a = a,b

    # now we work with a being the greater value :)
    # algorithm
    # A = B.Q + R
    # we just need to find Q and R
    # R == A mod B
    r = a % b
    # Q == quotient(a/b)
    q = a // b

    # recursively find gcd of B,R
    return euclidean_gcd(b,r)

gcd = euclidean_gcd(5,24)
