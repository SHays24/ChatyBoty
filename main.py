b = 0
i = 0
import sys
from pylint import epylint as lint
import time
from time import sleep


def printslow(str):
    for char in str:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


dictionary = {
    "redefining": "ignoring",
    "outer scope":
    "python but not exclusively your program(change name of variable)",
    "undefined": "variable not found create",
    "before assignment": "before the variable is defined",
    "unnecessary": "not needed",
    "EOL": "unenclosed string"
}

print('''
 ▄████████    ▄█    █▄       ▄████████     ███     ▄██   ▄   ▀█████████▄   ▄██████▄      ███     ▄██   ▄  
███    ███   ███    ███     ███    ███ ▀█████████▄ ███   ██▄   ███    ███ ███    ███ ▀█████████▄ ███   ██▄ 
███    █▀    ███    ███     ███    ███    ▀███▀▀██ ███▄▄▄███   ███    ███ ███    ███    ▀███▀▀██ ███▄▄▄███ 
███         ▄███▄▄▄▄███▄▄   ███    ███     ███   ▀ ▀▀▀▀▀▀███  ▄███▄▄▄██▀  ███    ███     ███   ▀ ▀▀▀▀▀▀███ 
███        ▀▀███▀▀▀▀███▀  ▀███████████     ███     ▄██   ███ ▀▀███▀▀▀██▄  ███    ███     ███     ▄██   ███ 
███    █▄    ███    ███     ███    ███     ███     ███   ███   ███    ██▄ ███    ███     ███     ███   ███ 
███    ███   ███    ███     ███    ███     ███     ███   ███   ███    ███ ███    ███     ███     ███   ███ 
████████▀    ███    █▀      ███    █▀     ▄████▀    ▀█████▀  ▄█████████▀   ▀██████▀     ▄████▀    ▀█████▀  '''
      )
printslow('\nHello, do you need help?\n')
yn = input('> ')
if yn == 'yes':
    printslow(
        'Could you please upload your code to my test files folder to recieve an easy to read error.\n'
    )
    time.sleep(5)
    printslow('Have you uploaded the code?\n')
    yn = input('> ')
while i == 0:
    if yn == 'yes':
        lint.py_run('test_files --output=text.txt', return_std=False)
        with open("text.txt", mode="r") as f:
            fin = f.read()
            fin = fin.lower()
            while b <= 4:
                for key in fin.split():
                    try:
                        result = fin.replace(key, dictionary[key])
                        b += 1
                    except KeyError:
                        continue

        i += 1
    if yn != 'yes':
        time.sleep(5)
    print(result)
