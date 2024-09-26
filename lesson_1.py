'''
lesson_1
'''
import chardet
import subprocess
import platform
import requests
import ast
'''
1. 
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
'''

words_1 = ['разработка', 'сокет', 'декоратор']

url = 'http://130.61.54.130'

def myencoder(string, url, coding='encode'):
    params = dict(action=coding,
                  value=string)
    res = requests.get(url, params=params)
    return res.text

def unicode_symbol(string):
    lst = string
    new_string = ''
    for i in lst:
        new_string += f"\\u{str('%04x' % ord(i))}"
    return new_string


for word in words_1:
    u_word = unicode_symbol(word)
    # u_word = myencoder(word, url)
    print(f'тип слова {word} - {type(word)}')
    print(f'тип слова {u_word} - {type(u_word)}')
    if word == u_word:
        print('Одинаковые')

'''
2. 
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

def str_to_byte(string):
      return ast.literal_eval(f"b'{string}'")

words_2 = ['class', 'function', 'method']

for word in words_2:
      print(type(str_to_byte(word)))

'''
3. 
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''

words_3 = ['attribute','класс','функция','type']

for word in words_3:
      try:
            print(type(str_to_byte(word)))
      except SyntaxError:
            print(f'слово {word} невозможно записать в байтовом типе')

'''
4. 
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в 
байтовое и выполнить обратное преобразование (используя методы encode и decode).
'''

words_4 = ['разработка', 'администрирование', 'protocol', 'standard']

def encode_str(string, coding, error='strict'):
      return string.encode(encoding=coding, errors=error)

def decode_str(string, coding, error='strict'):
      return string.decode(encoding=coding, errors=error)

for word in words_4:
      print(encode_str(word, 'utf-8'))
      print(decode_str(encode_str(word, 'utf-8'), 'utf-8'))

'''
5. 
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
'''

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
result = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in result.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

'''
6. 
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''
words_6 = ['сетевое программирование', 'сокет', 'декоратор']

with open('test.txt', 'w', encoding='utf-8') as f:
    for word in words_6:
        f.write(f'{word}\n')

with open('test.txt', 'rb') as f:
    content = f.read()
encoding = chardet.detect(content)['encoding']

with open('test.txt', encoding=encoding,) as f:
    for string in f:
        print(string, end='')

