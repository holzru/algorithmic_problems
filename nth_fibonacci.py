def mul(A, B):
    a, b, c = A
    d, e, f = B
    return a*d + b*e, a*e + b*f, b*e + c*f

def pow(A, n):
    n_new = abs(n)
    if n_new == 1:     return A
    if n_new & 1 == 0: return pow(mul(A, A), n_new//2)
    else:          return mul(A, pow(mul(A, A), (n_new-1)//2))

def fib(n):
    n_new = abs(n)
    if n > 0:
        if n < 2: return n
        return pow((1,1,0), n-1)[0]
    else:
        if n_new % 2 == 0:
            return -(pow((1,1,0), n_new-1)[0])
        else:
            return pow((1,1,0), n_new-1)[0]

print fib(96)
print fib(-96)
