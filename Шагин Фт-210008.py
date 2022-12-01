import random
import logging

logging.basicConfig(filename = "base_log.log", level=logging.INFO)

while True:
    try:
        num = int (input("Введите число больше 1:"))
        if num <= 0:
            print('неверный ввод\nповторите попытку')
        else:
            logging.info(f'количество бочонков:  {num}')
            break
    
    except ValueError:
        print('Неверный ввод\nповторите попытку')

num_list = [i+1 for i in range(num)]

random.shuffle(num_list)


for i in range(num):
    input('нажмите Enter для вывода следующего числа ')
    logging.info("кнопка нажата")
    print(num_list[i])
    logging.info(f"получено число: {num_list[i]}")

logging.info("программа завершена")
