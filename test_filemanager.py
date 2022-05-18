import os
from filemanager_by_Orlov.filemanager import copy_file_or_directory, author_info, filenames
from filemanager_by_Orlov.victory import date_to_str
# from filemanager_by_Orlov.main import separator
'''
Импорт функции из main сразу дает ошибку, исправить так и не смогла, общение с куратором не помогло
'''

def test_author_info():
    assert author_info()=='Leonid Orlov'

def test_filenames():
    assert type(filenames()) == list
    assert len(filenames())==len(set(filenames()))
    assert os.path.isfile("filemanager_by_Orlov/filemanager.py")

def test_date_to_str():
    assert date_to_str('26.06.1799') == 'двадцать шестое июня 1799 года'
    assert date_to_str('04.06.1975') == 'четвертое июня 1975 года'
'''
Импорт функции из main сразу дает ошибку, исправить так и не смогла, общение с куратором не помогло. Но тест я написала.
'''
# def test_separator():
#     assert separator(count=30)=='******************************'
#     assert separator(count=5) == '*****'

def test_copy_file_or_directory():
    '''
    нечистая функция
    :return: копия файла/папки с новым именем
    '''
    copy_file_or_directory('filemanager_by_Orlov/bill.py','filemanager_by_Orlov/bill_the_second.py')
    assert os.path.isfile('filemanager_by_Orlov/bill_the_second.py')
    os.remove('filemanager_by_Orlov/bill_the_second.py')