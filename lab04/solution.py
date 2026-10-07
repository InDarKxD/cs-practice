def winner(names: list[str], scores: list[float]) -> str:
    max_res, max_res_index = 0, 0
    for i in range(len(scores)):
        if scores[i] > max_res: max_res, max_res_index = scores[i], i
    return names[max_res_index]

def average(scores: list[float]) -> float:
    return sum(scores)/len(scores)

if __name__ == '__main__':
    source_names, source_scores = ['Аня', 'Боря', 'Вика'], [7.0, 9.0, 9.0]
    print(winner(names=source_names, scores=source_scores))
    print(average(scores=source_scores))