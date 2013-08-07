def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    #def n_ary_f(x, *args):
        #if len(args) == 0:
            #return x
        #return f(x,n_ary_f(args[0],*args[1:]))
    def n_ary_f(x, *args):
        return x if not args else f(x,n_ary_f(*args))
    return n_ary_f
