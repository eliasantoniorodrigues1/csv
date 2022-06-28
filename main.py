from typing import List, Dict
import csv
import io


def read_csv_list(file_name: str, encode='utf-8') -> List:
    '''
        read a csv file with default enconde utf-8
        return a list of list
        param: file_name: full path file
        param: opetional: encode: str
    '''
    with open(file_name, 'r', encoding=encode) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        return [row for row in spamreader]


def read_csv_dict(file_name: str, encode='utf-8') -> Dict:
    with open(file_name, encoding=encode) as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=';')
        return [row for row in spamreader]


if __name__ == '__main__':
    file_name = 'csv_test.csv'
    # consolidate = read_csv_list(file_name=file_name)
    consolidate = read_csv_dict(file_name=file_name)
    for value in consolidate:
        print(value)
