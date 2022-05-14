import os
import shutil
import sys
from my_module import *
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        if not os.path.exists('New'):
            os.mkdir('New')
    elif choice == '2':
        if os.path.exists('New'):
            os.rmdir('New')
    elif choice == '3':
        if os.path.exists('New'):
            shutil.copytree('New', 'Newest')
        else:
            print ('Такой папки не существует')
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        dirs=[]
        for dir in os.listdir():
            if os.path.isdir(dir):
                dirs.append(dir)
        print(list(dirs))
    elif choice == '6':
        files=[]
        for file in os.listdir():
            if os.path.isfile(file):
                files.append(file)
        print(list(files))
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print(os.getlogin())
    elif choice == '9':
        quiz()
    elif choice == '10':
        bank_account()
    elif choice == '11':
        os.chdir('c:/')
        print('Теперь рабочей директорией является' , os.getcwd())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
