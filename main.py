import tkinter as tk

#TODO sto ako kliknemo više operacija? - uzimamo zadnju operaciju koja je kliknuta
#TODO kombiniranje više operacija 2 + 3 / 4 - 9


math_expression = ''


def insert_one():
    global math_expression
    math_expression += '1'
    lbl_display_var.set(math_expression)

def insert_two():
    global math_expression
    math_expression += '2'
    lbl_display_var.set(math_expression)
  
def insert_three():
    global math_expression
    math_expression += '3'
    lbl_display_var.set(math_expression)

def insert_add():
    global math_expression
    math_expression += ' + '
    lbl_display_var.set(math_expression)
   
def insert_four():
    global math_expression
    math_expression += '4'
    lbl_display_var.set(math_expression)
    
def insert_five():
    global math_expression
    math_expression += '5'
    lbl_display_var.set(math_expression)
  
def insert_six():
    global math_expression
    math_expression += '6'
    lbl_display_var.set(math_expression)
   
def insert_subtract():
    global math_expression
    math_expression += ' - '
    lbl_display_var.set(math_expression)
   
def insert_seven():
    global math_expression
    math_expression += '7'
    lbl_display_var.set(math_expression)
 
def insert_eight():
    global math_expression
    math_expression += '8'
    lbl_display_var.set(math_expression)
  
def insert_nine():
    global math_expression
    math_expression += '9'
    lbl_display_var.set(math_expression)
  
def insert_multiply():
    global math_expression
    math_expression += ' * '
    lbl_display_var.set(math_expression)
   
def insert_clear():
    global math_expression
    math_expression = ''
    lbl_display_var.set('-')


def insert_zero():
    global math_expression
    math_expression += '0'
    lbl_display_var.set(math_expression)
    
def calculate():
    #prepoznati matematičku operaciju
    global math_expression
    if '+' in math_expression:
        first, last = math_expression.split(' + ')
        lbl_display_var.set(str((int(first) + int(last))))
    elif '-' in math_expression:
        first, last = math_expression.split(' - ')
        lbl_display_var.set(str((int(first) - int(last))))
    elif '*' in math_expression:
        first, last = math_expression.split(' * ')
        lbl_display_var.set(str((int(first) * int(last))))
    elif '/' in math_expression:
        first, last = math_expression.split(' / ')
        print(first)
        print(last)
        if last != '0':
            lbl_display_var.set(str((int(first) / int(last))))
        else:
            lbl_display_var.set('Dijeljenje s nulom')
    else:
         lbl_display_var.set('Operacija ne postoji')
        
    
 
def insert_division():
    global math_expression
    math_expression += ' / '
    lbl_display_var.set(math_expression)
    



main_window = tk.Tk()
main_window.title('Python Calculator')
# main_window.geometry('600x400')

main_window.columnconfigure((0, 1, 2, 3), minsize=75)
main_window.rowconfigure(0, minsize=100)
main_window.rowconfigure((1, 2, 3, 4), minsize=75)

#PROSTOR ZA WIDGETE
lbl_display_var = tk.StringVar()
lbl_display_var.set('_')
lbl_display = tk.Label(main_window,
                       textvariable=lbl_display_var,
                       anchor='e',
                       justify=tk.LEFT,
                       font=('Segoe UI', 20)).grid(row=0, column=0, columnspan=4)

# for i in range(4):
#     for i in range(5):
btn_one = tk.Button(main_window,
                    text='1',
                    font=('Segoe UI', 12),
                    command=insert_one).grid(column=0, row=1, sticky='NESW') #NESW strane svijeta-maksimizirano na sve osi, kako će se zalijepti za ćelije unutar grida, za koje rubove će se zalijepit
btn_two = tk.Button(main_window,
                    text='2',
                    font=('Segoe UI', 12),
                    command=insert_two).grid(column=1, row=1, sticky='NESW')
btn_three = tk.Button(main_window,
                    text='3',
                    font=('Segoe UI', 12),
                    command=insert_three).grid(column=2, row=1, sticky='NESW')
btn_add = tk.Button(main_window,
                    text='+',
                    font=('Segoe UI', 12),
                    command=insert_add).grid(column=3, row=1, sticky='NESW')
btn_four = tk.Button(main_window,
                    text='4',
                    font=('Segoe UI', 12),
                    command=insert_four).grid(column=0, row=2, sticky='NESW')
btn_five = tk.Button(main_window,
                    text='5',
                    font=('Segoe UI', 12),
                    command=insert_five).grid(column=1, row=2, sticky='NESW')
btn_six = tk.Button(main_window,
                    text='6',
                    font=('Segoe UI', 12),
                    command=insert_six).grid(column=2, row=2, sticky='NESW')
btn_substract = tk.Button(main_window,
                    text='-',
                    font=('Segoe UI', 12),
                    command=insert_subtract).grid(column=3, row=2, sticky='NESW')
btn_seven = tk.Button(main_window,
                    text='7',
                    font=('Segoe UI', 12),
                    command=insert_seven).grid(column=0, row=3, sticky='NESW')
btn_eight = tk.Button(main_window,
                    text='8',
                    font=('Segoe UI', 12),
                    command=insert_eight).grid(column=1, row=3, sticky='NESW')
btn_nine = tk.Button(main_window,
                    text='9',
                    font=('Segoe UI', 12),
                    command=insert_nine).grid(column=2, row=3, sticky='NESW')
btn_multiply = tk.Button(main_window,
                    text='*',
                    font=('Segoe UI', 12),
                    command=insert_multiply).grid(column=3, row=3, sticky='NESW')
btn_clear = tk.Button(main_window,
                    text='C',
                    font=('Segoe UI', 12),
                    command=insert_clear).grid(column=0, row=4, sticky='NESW')
btn_zero = tk.Button(main_window,
                    text='0',
                    font=('Segoe UI', 12),
                    command=insert_zero).grid(column=1, row=4, sticky='NESW')
btn_calculate = tk.Button(main_window,
                    text='=',
                    font=('Segoe UI', 12),
                    command=calculate).grid(column=2, row=4, sticky='NESW')
btn_division = tk.Button(main_window,
                    text='/',
                    font=('Segoe UI', 12),
                    command=insert_division).grid(column=3, row=4, sticky='NESW')
main_window.mainloop()