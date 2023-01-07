import tkinter as tk
import openpyxl

filename = "data.xlsx"


def input():
    filename = "data.xlsx"
    try:
        wb = openpyxl.load_workbook(filename)
        sheet = wb.active
        data = []
        for row in sheet.rows:
            data_row = []
            for cell in row:
                data_row.append(cell.value)
            data.append(data_row)
        print(data)
    except FileNotFoundError:
        print("Файл не найден")


master = tk.Tk()
tk.Label(master, text="Имя файла").grid(row=0)

e1 = tk.Entry(master)
e1.grid(row=0, column=1)

tk.Button(master, text='ОК', command=input()).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
