from utils import *
from os.path import exists


def main():
    while True:
        path = 'phone.csv'
        step = input("Введите действие: ")
        if step == 'q':
            break
        elif step == 'w':

            flag = exists(path)
            if not flag:
                creating()
                record_info()
            else:
                record_info()

        elif step == 'r':
            print(reading_csv(path))

main()
