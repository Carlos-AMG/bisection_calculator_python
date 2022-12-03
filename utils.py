import numpy as np
import scipy.special as special

symbols = {
    "e**": "np.exp",
    "cos" : "np.cos",
    "tan" : "np.tan", 
    "sin" : "np.sin",
    "arcsin" : "np.arcsin", 
    "arccos" : "np.arcos",
    "arctan" : "np.arctan",
    "**": "np.exp",
    "log" : "np.log",
    "log2" : "np.log2",
    "log10": "np.log10"
}

def crear_func(expr):
    funcstr = (f"""def f(x):
    return {expr}""")
    exec(funcstr)
    return locals().get("f")

# f = make_func(expr)
# dynamicF = f(1.4)
# originalF = original(1.4)
# print(dynamicF)
# print(originalF)
# print(originalF == dynamicF)