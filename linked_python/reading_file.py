


def open_file():
# открыть файл для записии создать его если он не существует
    myfile = open("textfile.txt", "w")
    myfile.close()
def add_lines_in_file():
    # Открыть файл для того чтобы добавить строки в конце
    myfile = open("textfile.txt", "a")
    # Написать что нибудь в файл
    for i in range(5, 10):
        myfile.write("This is the some text in file\n")

    # закрыть файл
    myfile.close()
# открыть файл на чтение. Если открываем файл на чтение, то нет необходимости его закрывать
def open_file_for_read():
    myfile = open("textfile.txt", "r")
    if myfile.mode == "r":
        contents = myfile.read()
        print(contents)
#  вывод на печать построчно
def print_line_by_line():
    myfile = open("textfile.txt", "r")
    if myfile.mode == "r":
        f1 = myfile.readlines()
        for x in f1:
            print(x)
print_line_by_line()