import os
from os import path
import datetime
import shutil
from shutil import make_archive
from datetime import date, time, timedelta
from zipfile import ZipFile

#  работа с путем
def main():
#     распечатаь название ОС
    print(os.name)
    myfile = open("textfile.txt", "w")
    myfile.close()
#     проверить существование элемента
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file:", path.isfile("textfile.txt"))
    print("Item is a directory:", path.isdir("textfile.txt"))
#     работа с путем файла
#     путь к текущей директории
    print(os.getcwd())
#     полный путь к файлу
    print("Item's path:", path.realpath("textfile.txt"))
    print("Item's path and name:", path.split(path.realpath("textfile.txt")))
    a = path.split(path.realpath("textfile.txt"))
    print(a[0])
#     получить время изменения файла

# получичаем дату файла
def get_modification_time():
    # получаем дату последнего изменения файла
    t = datetime.datetime.fromtimestamp(os.path.getmtime("textfile.txt"))
    print(t)
#     вычислить разницу между текущим временем и датой изменения файла
    td = datetime.datetime.now() - t
    return print(td.total_seconds(), "seconds")

#  работа с файлом (создать: дубликат, копию, переименовать,

def using_filesystem_shell_method():
#      проверяем что файл существует
    if path.exists("textfile.txt.bak"):
# #         получить полный путь к файлу
        src = path.realpath("textfile.txt")
#         создать копию файла , бэкап с *.bak
        dst = src + ".bak"
#         первый аргумент = путь, второй копия
        shutil.copy(src, dst)
#         переименовать файл
        os.rename("textfile.txt", "newfile.txt")


#  создать архив(в который входят все файлы и архив который входят несколько файлов)
def make_archive_with_all_files():
#      проверяем что файл существует
    if path.exists("textfile.txt.bak"):
# #         получить полный путь к файлу
        src = path.realpath("textfile.txt.bak")
#         заархивировать файл
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

#  создать архив(в который входят несколько файлов)
def make_archive_with_some_files():
#      проверяем что файл существует
    if path.exists("textfile.txt.bak"):
# #         получить полный путь к файлу
        src = path.realpath("textfile.txt.bak")
#         заархивировать файл
        root_dir, tail = path.split(src)

        with ZipFile("test.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")


def calculate_all_files_in_dir():
    totalbytes = 0
    folder = "..\\linked_python"
    dirlist = os.listdir("..\\linked_python")
    for entry in dirlist:
        if os.path.isfile(folder + "//" + entry):
            print(entry)
            filesize = os.path.getsize(folder + "//" + entry)
            totalbytes += filesize
    print(os.listdir())
    return totalbytes



calculate_all_files_in_dir()