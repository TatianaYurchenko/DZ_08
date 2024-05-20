import os
def main_1():
    hestr = "Ogres are often foolhardy oafs"
    newstr = ""
    for i, c in enumerate(hestr):
        if c == "o":
            continue
        if i > 20:
            break
        newstr += c
    print(newstr)
def string_up():
    var = "123456789"
    print(var[1:6:2])

def is_palindrome(s):
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    print(s[::-1])
    if s == s[::-1]:
        print(True)
    else:
        print(False)


