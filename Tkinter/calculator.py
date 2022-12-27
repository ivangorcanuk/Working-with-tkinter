import tkinter as tk

win = tk.Tk()
win.geometry(f'240x260+100+200')  # создаем окно, указываем размеры
# win.bq = '#33ffe6'  # создаем цвет фона
win.title('Calculator')  # называем окно

"""Создаем наш ввод"""

calc = tk.Entry(win)  # создаем экземпляр класса Entry
calc.grid(row=0, column=0, columnspan=3)  # создаем таблицу(адрес первой ячейки, ряд по горизонтали=0, и по вертикали=0. Объеденили 3 колонки)

"""Создаем наши кнопки"""

tk.Button(text='1').grid(row=1, column=0)
tk.Button(text='2').grid(row=1, column=1)
tk.Button(text='3').grid(row=1, column=2)
tk.Button(text='4').grid(row=2, column=0)
tk.Button(text='5').grid(row=2, column=1)
tk.Button(text='6').grid(row=2, column=2)
tk.Button(text='7').grid(row=3, column=0)
tk.Button(text='8').grid(row=3, column=1)
tk.Button(text='9').grid(row=3, column=2)
tk.Button(text='0').grid(row=4, column=0)

win.mainloop()