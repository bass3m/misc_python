def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1

# this is really a squareroot not the inverse
def sqrt(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def good_enough(guess,y):
        return True if abs(f(guess) - y) < delta else False
    def f_1(y):
        guess = 1
        while not good_enough(guess,y):
            guess = (guess + (y/guess)) / 2.
        return guess
    return f_1

# Peter Norvig's solution
def official_inverse(f, delta = 1/1024.):
    def f_1(y):
        lo, hi = bounds(f,y)
        return binary_search(f,y,lo,hi,delta)
    return f_1
def bounds(f,y):
    x = 1
    while f(x) < y:
        x = x * 2
    lo = 0 if (x == 1) else x/2.
    return lo,x
def binary_search(f,y,lo,hi,delta):
    while lo <= hi :
        x = (lo + hi)/2.
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else:
            return x
    return hi if (f(hi) - y < y - f(lo)) else lo

# my answer
def inverse(f, delta = 1/1024.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def good_enough(guess,y):
        return True if abs(guess - y) < delta else False
    def find_bounds(x,y):
        # double until we reach a value where f(x) > y
        while (f(x) < y):
            x *= 2
        return (x/2, x) # return lo and hi range
    def search_bounds(lo,hi,y):
        mid = (lo + hi) / 2.
        guess = f(mid)
        if good_enough(guess,y):
            return mid
        return search_bounds(mid,hi,y) if guess < y else search_bounds(lo,mid,y)
    def f_1(y):
        lo, hi = find_bounds(1,y) # start with 1 as our guess
        return search_bounds(lo,hi,y)
    return f_1

def square(x): return x*x
sqrt = sqrt(square)
def cube(x): return x*x*x
cuberoot = inverse(cube)
#print sqrt(1000000000)
#print cuberoot(8)
