def count_items(values: list) -> dict:
    res = {}
    for element in list(set(values)): res[element] = values.count(element)
    return res

def unique_sorted(values: list) -> list:
    return sorted(list(set(values)))

def common(first: list, second: list) -> list:
    return unique_sorted(first+ second)

def only_in_first(first: list, second: list) -> list:
    res = []
    for i in first:
        if i not in second: res.append(i)
    return res