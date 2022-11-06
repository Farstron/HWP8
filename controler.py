import view 
import module
stop = False
def work_space(path):
    global stop    
    if path == '':
        path = view.reqest('Укажите имя и формат файла: ')
        module.path_format(path)
        reader()
    actions(view.show_menu(),path, module.format)
    if stop != True:
        return work_space(path)
        
def reader():
    if module.format == 'csv':
        module.DATA(module.read_csv())
    else:
        if module.format == 'json':
            module.DATA(module.read_json())

def writer(data):
    if module.format == 'csv':
        module.write_csv(data)
    else:
        if module.format == 'json':
            module.write_json(data)

def actions(NA, path, format):
    NA = int(NA)
    if NA > 9 or NA < 1:
       return actions(view.reqest('Такого действия нет! Выберите действие из списка:'),path, format)
    else:
        if NA == 1:
            find_emp(module.data)
        if NA == 2:
            area_position(module.data)
        if NA == 3:
            area_find_salary(module.data)
        if NA == 4:
            add_emp(module.data)
        if NA == 5:
            del_emp(module.data)
        if NA == 6:
            refresh(module.data)
        if NA == 7:
            to_json(module.data)
        if NA == 8:
            to_csv(module.data)
        if NA == 9:
            view.console_write('Всего хорошего!')
            global stop
            stop = True

def find_emp(data):
    FIO = view.reqest('Введите ФИО работника: ').split()
    pers = ['','']
    pers[0] += FIO[0]
    pers[1] += FIO[1]
    inf = []
    if len(FIO) == 3:
        pers[1] += ' ' + FIO[2]
    for i in data:
        if i.get('last_name') == pers[0] and i.get('first_name') == pers[1]:
            temp = list(i.values())
            inf.append(view.send_to_str(temp))
    view.console_write(''.join(inf))

def area_find_salary(data):
    salary = view.reqest('Введите диапазон зарплаты:').split()
    inf = []
    for i in data:
        if i.get('salary') >= int(salary[0]) and i.get('salary') <= int(salary[1]):
            temp = list(i.values())
            inf.append(view.send_to_str(temp))
    view.console_write(''.join(inf))

def area_position(data):
    position = view.reqest('Введите должность: ')
    inf = []
    for i in data:
        if i.get('position') == position:
            temp = list(i.values())
            inf.append(view.send_to_str(temp))
    view.console_write(''.join(inf))

def to_csv(data):
    module.write_csv(data)

def to_json(data):
    module.write_json(data)

def add_emp(data):
    print(data)
    emp = view.reqest('Введите фамилию, имя и отчество, должность, номер телефона, зарплату работника через запятую (кроме имя и отчества): ').split(', ')
    id = 1
    for i in data:
        if id != i.get('id'):
            break
        else:
            id+=1
    temp = {}
    temp["id"] = id
    temp["last_name"] = emp[0]
    temp["first_name"] = emp[1]
    temp["position"] = emp[2]
    temp["phone_number"] = emp[3]
    temp["salary"] = float(emp[4])
    data.append(temp)
    writer(data)

def del_emp(data):
    FIO = view.reqest('Введите ФИО работника: ').split()
    pers = ['','']
    pers[0] += FIO[0]
    pers[1] += FIO[1]
    if len(FIO) == 3:
        pers[1] += ' ' + FIO[2]
    for i in data:
        if i.get('last_name') == pers[0] and i.get('first_name') == pers[1]:
            data.remove(i)
    writer(data)

def refresh(data):
    FIO = view.reqest('Введите ФИО работника: ').split()
    pers = ['','']
    pers[0] += FIO[0]
    pers[1] += FIO[1]
    ch = view.reqest('Что вы хотите обновить?(last_name, first_name, position, phone_number, salary) ').split(', ')
    inf = view.reqest('Какие значения внести?(Антон, 777 и т.д.) ').split(', ')
    if len(FIO) == 3:
        pers[1] += ' ' + FIO[2]
    for i in data:
        if i.get('last_name') == pers[0] and i.get('first_name') == pers[1]:
            temp = i
            for j in range(0,len(ch)):
                temp[ch[j]] = inf[j]
            data.remove(i)
            data.append(temp)
    writer(data)
