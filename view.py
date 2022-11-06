def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def reqest(req):
    return input(req)

def send_to_str(send):
    ts = ''
    ts += str(send[0])+' '
    ts += str(send[1])+' '
    ts += str(send[2])+' '
    ts += str(send[3])+' '
    ts += str(send[4])+' '
    ts += str(send[5])+'\n'
    return ts

def console_write(send):
    print(send)