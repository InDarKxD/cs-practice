import csv

def read_rows(lines): return list(csv.DictReader(lines))

