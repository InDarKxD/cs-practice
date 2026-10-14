def read_rows(lines: list[str]) -> list[dict]:
    header, container = [], []
    for line in lines:
        line = line.rstrip('\n').rstrip('\r')
        if line == '': continue
        line = line.split(',')
        if len(line) != 3: continue
        if header == []:
            header = line
            continue
        container.append({header[0]: line[0], header[1]: line[1], header[2]: float(line[2])})
    return container

def count_types(rows: list[dict]) -> dict:
    status_count = {}
    for row in rows:
        if row['тип'] not in status_count.keys(): status_count[row['тип']] = 0
        else: status_count[row['тип']] += 1
    return status_count

def total_minutes(rows: list[dict], kind: str) -> float:
    time = 0.0
    for row in rows:
        time += row['минуты'] if row['тип'] == kind else 0.0
    return f'{time:.1f}'

def to_csv(counts: dict) -> str: return f'тип,количество\nвыгрузка,{counts['выгрузка']}\nзапуск,{counts['запуск']}\nошибка,{counts['ошибка']}\nпроверка,{counts['проверка']}'