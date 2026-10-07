def winner(names: list[str], scores: list[float]) -> str:
    if len(names) != len(scores) or len(scores) == 0: return ''
    max_res, max_res_index = scores[0], 0
    for i in range(1, len(scores)):
        if scores[i] > max_res: max_res, max_res_index = scores[i], i
    return names[max_res_index]

def average(scores: list[float]) -> float:
    if len(scores) == 0: return 0
    return round(sum(scores)/len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    names_copy, scores_copy, result = names.copy(), scores.copy(), []
    if len(names_copy) != len(scores_copy): return []
    while len(scores_copy) != 0:
        max_elem_index = scores_copy.index(max(scores_copy))
        result.append(names_copy.pop(max_elem_index))
        scores_copy.pop(max_elem_index)
    return result

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg, result = average(scores=scores), []
    if len(names) != len(scores): return []
    for i in range(len(scores)):
        if scores[i] > avg: result.append(names[i])
    return result

if __name__ == '__main__':
    source_names, source_scores = ['Аня', 'Боря', 'Вика'], [7.0, 9.0, 9.0]
    print(winner(names=source_names, scores=source_scores))
    print(average(scores=source_scores))
    print(ranking(names=source_names, scores=source_scores))
    print(above_average(names=source_names, scores=source_scores))