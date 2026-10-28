from numpy import *

def reshape_rows(values, width):
    res = asarray(values, dtype=float)
    if res.size == 0 or width <= 0 or res.size % width != 0: return []
    res = round(res.reshape(-1, width), 6).tolist()
    return res
