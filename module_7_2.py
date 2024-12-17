from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    # определяем начальные значения
    string_positions = {}   # задаём словарь
    str_num = 0
    str_start_byte = file.seek(0)   # байт начала первой строки
    for string_ in strings:
        file.write(string_+'\n')
        str_num += 1
        key = (str_num, str_start_byte) # задаём ключи словаря
        string_positions[key]= string_  # добавляем значения в словарь
        str_start_byte = file.tell()
    file.close()
    return string_positions

file_name = 'newfile.txt'   # задаём имя нашего файла
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

