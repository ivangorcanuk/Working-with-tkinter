import tkinter as tk
from tkinter import messagebox

# запретить растягивать окно
# убрать кнопку развернуть
# запретить вводить цифры вручную
# добавить рефреш
# уменьшить отступы между кнопками

def add_digit(digit):  # функция добавляет числа при нажатии на кнопки
    value = calc.get()  # сохраняем добавленную строку
    if value[0] == '0' and len(value) == 1:  # если выражение начинается с 0 и размер его 1 символ
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)  # очищаем наш ввод
    calc.insert(0, value + digit)  # добавляем новое значение
    calc['state'] = tk.DISABLED

def add_operation(operation):  # функция добавляет операцию при нажатии на кнопку
    value = calc.get()
    if value[-1] in '+-*/':  # если последний добавленный символ это операция
        value = value[:-1]  # сохраняем все кроме самоц операции
    elif '+' in value or '-' in value or '*' in value or '/' in value:  # если в выражении уже присутствует операция
        calculate()  # высчитываем
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)  # добавляем новое значение
    calc['state'] = tk.DISABLED

def calculate():  # функция высчитывает выражение при нажатии на кнопку
    value = calc.get()  # сохраняем добавленную строку
    if value[-1] in '+-*/':  # если выражение закончилось операцией
        value = value[:-1] + value[-1] + value[:-1]  # первую часть выражения добавляем в нехватающую
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))  # eval подсчитывает выражение несмотря на стороковый тип
        calc['state'] = tk.DISABLED
    except ZeroDivisionError:  # отловили ошибку
        messagebox.showinfo('Внимание','На 0 делить нельзя')
        calc.insert(0, '0')
        calc['state'] = tk.DISABLED

def clear():  # функция очищает строку ввода
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')  # устанавливаем значение 0
    calc['state'] = tk.DISABLED

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial',13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',13), fg='red', command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',13), fg='red', command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',13), fg='red', command=clear)

def press_key(event):
    print(event)

win = tk.Tk() # создаем окно
win.geometry(f'240x271+100+200')  # указываем размеры
win['bg'] = '#33ffe6'  # задаем цвет фона
win.title('Calculator')  # называем окно
win.resizable(False, False)  # запретить растягивать окно, убрать кнопку развернуть

win.bind('<Key>', press_key)  # обрабатываем события (<Key> тип событий - любое нажатие на клавишу, вызываем функцию, которая обработает это событие)

"""Строка ввода"""

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',15), width=15)  # создаем экземпляр класса Entry. justify текст при вводе прижимается к правой стороне, а не к левой. font изменили шрифт строки ввода, width ограничение на 15 символов
calc.insert(0, '0')  # добавили 0 в строку ввода
calc['state'] = tk.DISABLED  # состояние строки установили неактивным, теперь нельзя поставить курсор
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5, pady=2)  # создаем таблицу(адрес первой ячейки, ряд по горизонтали=0, и по вертикали=0. Объеденили 4 колонки)

"""Кнопки с цифрами"""

make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=2, pady=2)  # sticky растянули кнопки на Св, Юг, Зп, Вс.
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=2, pady=2)  # padx, pady добавили отступы между кнопками по x и y
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=2, pady=2)  # bd добавили рамки для кнопок
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=2, pady=2)  # вызываем lambda, которая вызывает функцию add_digit, она дает кнопкам свой символ при нажатии на нее
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=2, pady=2)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=2, pady=2)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=2, pady=2)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=2, pady=2)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=2, pady=2)
make_digit_button('0').grid(row=4, column=0, sticky='wens', padx=2, pady=2)

"""Кнопки с операциями"""

make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=2, pady=2)
make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=2, pady=2)
make_operation_button('*').grid(row=3, column=3, sticky='wens', padx=2, pady=2)
make_operation_button('/').grid(row=4, column=3, sticky='wens', padx=2, pady=2)

"""Кнопка подсчитывания"""

make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=2, pady=2)

"""Кнопка рефреш"""

make_clear_button('c').grid(row=4, column=1, sticky='wens', padx=2, pady=2)

win.grid_columnconfigure(0, minsize=60)  # задаем минимальный размер колонки
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)  # задаем минимальный размер ряда
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()