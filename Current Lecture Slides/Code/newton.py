def d(f):
    dx = 10**(-10)
    return lambda x:(f(x+dx)-f(x))/dx

def newton(g):
    x = 999
    err = 10**(-10)
    while abs(g(x))> err:
        x = x-g(x)/d(g)(x)

    return x
