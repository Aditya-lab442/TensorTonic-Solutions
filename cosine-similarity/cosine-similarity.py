import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dotProd=0
    for i in range(len(a)):
        dotProd+=(a[i]*b[i])
    if dotProd == 0:
        return 0.0
    # Calculate Euclidean norms.
    
    a2 = 0
    for i in a:
        a2+=(i**2)
    a2 = a2**0.5

    b2 = 0
    for i in b:
        b2+=(i**2)
    b2 = b2**0.5
    return dotProd/(a2*b2)
    pass