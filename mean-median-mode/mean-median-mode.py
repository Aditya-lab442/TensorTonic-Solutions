from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    # ans = np.array(x)
    ans = dict()
    ans['mean'] = float(np.mean(x))
    ans['median'] = float(np.median(x))
    temp = dict()
    for i in x:
        temp[i] = x.count(i)
    maxValue = max(temp.values())
    for i,j in temp.items():
        if j == maxValue:
            ans['mode'] = float(i)
            break;
    return ans
    pass