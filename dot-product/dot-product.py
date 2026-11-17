import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    dotProd = 0
    for i in range(len(x)):
        dotProd+=(x[i]*y[i])
    return float(dotProd)
    pass