'''
lesson 2
'''
import os
from glob import glob
from chardet.universaldetector import UniversalDetector
import csv
import json
import yaml
import re
from datetime import datetime
'''
1. 
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов 
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. 
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в 
соответствующий список. Должно получиться четыре списка — например, 
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для 
хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка: 
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить 
в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. 
В этой функции реализовать получение данных через вызов функции get_data(), 
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
'''

os.chdir('.')
names = glob('*.txt')


def detector_coding(file:str):
    '''
    :param file: filename > 'file.txt'
    :return: coding > 'utf-8'
    '''
    detector = UniversalDetector()
    detector.reset()
    for line in open(file, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']


def get_data(list_files:list):
    '''

    :param list_files: list with filenames
    :return: list
    '''
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for name in list_files:
        encoding = detector_coding(name)
        with open(name, 'r', encoding=encoding) as f:
            string_file = f.read()

            for line in string_file.split('\n'):
                if re.fullmatch(r'^Изготовитель системы.+', line):
                    os_prod_list.append(re.search(r'[A-Z].+', line)[0])
                if re.fullmatch(r'^Название ОС.+', line):
                    os_name_list.append(re.search(r'[A-Z].+', line)[0])
                if re.fullmatch(r'^Код продукта.+', line):
                    os_code_list.append(re.search(r'\d{5}.\w{3}.\d{7}.\d{5}', line)[0])
                if re.fullmatch(r'^Тип системы.+', line):
                    os_type_list.append(re.search(r'x\d\d.+', line)[0])

    for prod, name, code, type in zip(os_prod_list, os_name_list, os_code_list, os_type_list):
        main_data.append([prod, name, code, type])

    return main_data


def write_to_csv(file:str):
    '''
    :param file: filename > 'file.csv'
    '''
    with open(file, 'w',encoding='utf-8') as f:
        f_writer = csv.writer(f)
        for row in get_data(names):
            f_writer.writerow(row)


'''
2. 
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. 
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), 
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных 
в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''

def write_order_to_json(item:str, quantity:int, price:float, buyer:str, date:datetime):
    '''
    write dict to json
    :param item: str
    :param quantity: int
    :param price: float
    :param buyer: str
    :param date: datetime
    '''
    dict_to_json = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(dict_to_json, f, indent=4, ensure_ascii=False)


'''
3. 
Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных 
в файле YAML-формата. Для этого:

Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, 
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, 
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. 
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, 
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
'''





if __name__ == '__main__':
    write_to_csv('test.csv')
    write_order_to_json('Товар', 54, 5000.00, 'Иванов И.И.', '08/02/2022')

