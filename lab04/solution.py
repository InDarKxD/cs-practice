def winner(names: list[str], scores: list[float]) -> str:
    max_res, max_res_index = 0, 0
    for i in range(len(scores)):
        if scores[i] > max_res: max_res, max_res_index = scores[i], i
    return names[max_res_index]

def average(scores: list[float]) -> float:
    return sum(scores)/len(scores)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    scores_copy, result = scores.copy(), []
    while max(scores_copy) != -1:
        max_elem_index = scores_copy.index(max(scores_copy))
        result.append(names[max_elem_index])
        scores_copy[max_elem_index] = -1
    return result

    

if __name__ == '__main__':
    source_names, source_scores = ['Аня', 'Боря', 'Вика'], [7.0, 9.0, 9.0]
    print(winner(names=source_names, scores=source_scores))
    print(average(scores=source_scores))
    print(ranking(names=source_names, scores=source_scores))