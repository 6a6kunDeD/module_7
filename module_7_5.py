import os, time
from os.path import join, getmtime, getsize, dirname
directory = "."     # тестировать будем в папке проекта
for root, dirs, files in os.walk(directory):    # 1
    for file in files:
        filepath = os.path.join(root, file)     # 2
        filetime = os.path.getmtime(file)       # 3
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)        # 4
        parent_dir = os.path.dirname(os.path.abspath(file)) # полный путь
        # parent_dir = os.path.dirname(directory)  # относительный путь # 5
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f'Родительская директория: {parent_dir}')

# Комментарии к заданию:
#
# Ключевая идея – использование вложенного for
#
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},
#             Родительская директория: {parent_dir}')
#
#
#
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего
# в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11,
#   Родительская директория.