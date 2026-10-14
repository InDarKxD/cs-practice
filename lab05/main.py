from tablestats import *
import sys

def main():
    with open(file=sys.stdin.readline().strip(), mode='r', encoding='utf-8') as file:
        file_read = read_rows(file.readlines())
        print(len(file_read))
        print(len(count_types(file_read)))
        print(total_minutes(file_read, 'ошибка'))
        with open(file='summary.csv', mode='w', encoding='utf-8') as file_write:
            file_write.write(to_csv(count_types(file_read)))

if __name__ == '__main__': main()