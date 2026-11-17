import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    ans = []
    for i in A[0]:
        ans.append([i])
    for i in range(1,len(A)):
        for j in range(len(A[i])):
            ans[j].append(A[i][j])
    return np.array(ans)
    pass
