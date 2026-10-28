from numpy import *

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    res = asarray(values, dtype=float)
    if res.size == 0 or width <= 0 or res.size % width != 0: return []
    res = round(res.reshape(-1, width), 6).tolist()
    return res

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    res = asarray(matrix, dtype=float)
    if res.size == 0: return []
    res = round(res[ix_(rows, columns)], 6).tolist()
    return res

def column_means(matrix: list[list[float]]) -> list[float]:
    res = asarray(matrix, dtype=float)
    if res.size == 0: return []
    res = round(res.mean(axis=0), 6).tolist()
    return res

def column_range(matrix: list[list[float]], column: int) -> float:
    input_data = asarray(matrix, dtype=float)
    if input_data.size == 0: return 0.0
    columns = input_data[:, column]
    res = round(float( columns.max() - columns.min() ), 6)
    return res