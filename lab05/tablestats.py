import csv

def read_rows(lines): return list(csv.DictReader(lines))

def count_types(rows):
    status_count = {'запуск': 0, 'проверка': 0, 'ошибка': 0, 'выгрузка': 0}
    for row in rows: status_count[row['тип']] += 1
    return status_count

def total_minutes(rows, kind):
    time = 0
    for row in rows: time += row['минуты'] if row['тип'] == kind else 0
    return time