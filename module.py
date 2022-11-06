import csv
import json

def read_csv() -> list:
    employee = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    employee = []
    with open('database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee

def write_csv(employees: list):
    with open('database.csv', 'w', encoding='utf-8') as fout:
        csv_writer = csv.writer(fout,delimiter = ',',lineterminator='\r')
        for employee in employees:
            csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open('database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')

def path_format(file):
    global format
    i = len(file) - 1
    while file[i] != '.':
        format += file[i]
        i -= 1
    format = ''.join(list(reversed(format)))

def DATA(inf):
    global data
    data = inf
    
data = ''
format = ''