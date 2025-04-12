HELP = """
help - напечатать справку по программе. 
add - добавить задачу в список (название задачи
запращиваем у пользователя).
show - напечатать все добавленные задачи. 
exit - выход из программы. """

tasks = []
today = []
tomorrow = []
other = []

run = True

while run == True:
    command = input("Введите команду: ")
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(tasks)
    elif command == 'add':
        task = input('Введите название задачи: ')
        tasks.append(task)
        data = input('Введите дату выполнения задачи: ')
        if data == 'Сегодня':
            today.append(task)
        elif data == 'Завтра':
            tomorrow.append(task)
        elif data == 'Другой день':
            other.append(task)
        print('Задача добавлена')
    elif command == 'exit':
        print('Спасибо за использование!')
        break
    else:
        print('Неизвестная команда')
        break

print('До свидания!')