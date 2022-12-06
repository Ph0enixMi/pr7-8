import tkinter as tk
import psycopg2
from config import host1, user1, password1, db_name1
from tkinter import ttk
import datetime

connection = psycopg2.connect(host=host1, user=user1, password=password1, database=db_name1)
cursor = connection.cursor()
connection.autocommit = True

def employee():
    global win3
    win3 = tk.Toplevel()
    win3.protocol("WM_DELETE_WINDOW", on_closing1)
    win3.title('Сотрудник')
    win3.config(bg='#282828')
    win3.geometry('50x100+100+100')
    win.withdraw()

    button_em_task = tk.Button(win3, text='Задачи',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=button_em_task_click).grid(
        row=0, column=0, sticky='we')

def manager():
    global win4
    win4 = tk.Toplevel()
    win4.protocol("WM_DELETE_WINDOW", on_closing3)
    win4.title('Менеджер')
    win4.config(bg='#282828')
    win4.geometry('500x600+100+100')
    win.withdraw()

    button_employee = tk.Button(win4, text='Персонал',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_4Click).grid(
        row= 0, column=0, sticky='we')
    button_task = tk.Button(win4, text='Задания',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_manager_task).grid(
        row=1, column=0, sticky='we')
    button_create = tk.Button(win4, text='Создать задание',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_create).grid(
        row=2, column=0, sticky='we')
    button_client = tk.Button(win4, text='Клиенты',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_client).grid(
        row=3, column=0, sticky='we')  
    button_empl_ot = tk.Button(win4, text='Отчет по сотрудникам',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_empl_ot).grid(
        row=4, column=0, sticky='we')
    button_task_ot = tk.Button(win4, text='Отчет по задачам',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_task_ot).grid(
        row=5, column=0, sticky='we')
  
def btn_2Click():
    #Окно регистрации
    global win2
    win2 = tk.Toplevel()
    win2.protocol("WM_DELETE_WINDOW", on_closing2)
    win2.title('Регистрация')
    win2.config(bg='#282828')
    win2.geometry('350x370+100+100')
    win2.resizable(False, False)

    label_Name = tk.Label(win2, text='Имя:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=0, column=0, sticky='e')
    label_Pat = tk.Label(win2, text='Отчество:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=1, column=0, sticky='e')
    label_Surname = tk.Label(win2, text='Фамилия:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=2, column=0, sticky='e')
    label_phone = tk.Label(win2, text='Номер телефона:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=3, column=0, sticky='e')
    label_email = tk.Label(win2, text='Почта:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=4, column=0, sticky='e')
    label_login = tk.Label(win2, text='Логин:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=5, column=0, sticky='e')
    label_password = tk.Label(win2, text='Пароль:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=6, column=0, sticky='e')

    global select 
    select = tk.StringVar()

    radiobutton_1= tk.Radiobutton(win2, text= 'Сотрудник', bg='#282828', fg='white', font=('Calibri Light', 14), activebackground='#181818', activeforeground='white',variable=select, value='employe', pady=7, selectcolor='#181818').grid(
        row=7, column=0)
    radiobutton_2= tk.Radiobutton(win2, text= 'Менеджер', bg='#282828', fg='white', font=('Calibri Light', 14), activebackground='#181818', activeforeground='white',variable =select, value='manager', pady=7, selectcolor='#181818').grid(
        row=7, column=1)

    global entry_Name, entry_Pat, entry_Surname, entry_phone, entry_email, entry_login, entry_password

    entry_Name = tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_Pat = tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_Surname= tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_phone = tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_email = tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_login = tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_password = tk.Entry(win2, bg='#282828', fg='white', font=('Calibri Light', 14), show = '*')

    entry_Name.grid(row=0, column=1)
    entry_Pat.grid(row=1, column=1)
    entry_Surname.grid(row=2, column=1)
    entry_phone.grid(row=3, column=1)
    entry_email.grid(row=4, column=1)
    entry_login.grid(row=5, column=1)
    entry_password.grid(row=6, column=1)

    button_3 = tk.Button(win2, text='Ок',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_3Click, width=10).grid(
        row=8, column=1, sticky='e')

    win.withdraw()

def btn_3Click():
    global cursor
    #Получаем информацию с Entry
    if (entry_email.get != None and entry_login.get != None and entry_Surname.get != None and entry_Name.get != None and entry_Pat.get != None and entry_phone.get != None):
        cursor.execute(
            f"""insert into employees(login, password,employee_full_name, employee_phone_number, employee_email_address, post, employee_id) 
            values('{str(entry_login.get())}', crypt('{str(entry_password.get())}', gen_salt('md5')), '{str(entry_Surname.get())} {str(entry_Name.get())} {str(entry_Pat.get())}', '{str(entry_phone.get())}', '{str(entry_email.get())}', '{str(select.get())}', 6);"""
        )

    win.deiconify()
    win2.destroy()

def btn_4Click():
    #Выводит персонал
    global win5
    win5 = tk.Toplevel()
    win5.title('Персонал')
    win5.config(bg='#282828')
    win5.geometry('1420x600')

    cursor.execute("select count(*) from employees")
    rows = cursor.fetchall
    cursor.execute("select * from employees;")
    employees = cursor.fetchall()

    columns = ('employee_id', 'employee_full_name', 'employee_phone_number', 'employee_email_address', 'post', 'login', 'password')

    table = ttk.Treeview(win5, columns=columns, show='headings', height=400)
    table.grid(row=0, column=0, sticky="nsew")
    table.heading('employee_id', text='ID Сотрудника')
    table.heading('employee_full_name', text='ФИО')
    table.heading('employee_phone_number', text='Номер телефона')
    table.heading('employee_email_address', text='Почта')
    table.heading('post', text='Пост')
    table.heading('login', text='Логин')
    table.heading('password', text='Пароль')

    for employee in employees:
        table.insert("", 'end', values=employee)

    scrollbar = ttk.Scrollbar(win5, orient='vertical', command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

def btn_client():
    #Выводит клиентов
    global win6
    win6 = tk.Toplevel()
    win6.title('Клиенты')
    win6.config(bg='#282828')
    win6.geometry('1420x600')

    cursor.execute("select count(*) from clients;")
    rows = cursor.fetchall
    cursor.execute("select * from clients;")
    employees = cursor.fetchall()

    columns = ('client_id', 'company_name', 'client_phone_number', 'client_email_address', 'client_address', 'is_current')

    table = ttk.Treeview(win6, columns=columns, show='headings', height=400)
    table.grid(row=0, column=0, sticky="nsew")
    table.heading('client_id', text='ID клиента')
    table.heading('company_name', text='Название компании')
    table.heading('client_phone_number', text='Номер телефона')
    table.heading('client_email_address', text='Почта')
    table.heading('client_address', text='Адрес')
    table.heading('is_current', text='Потенциальнй')

    for employee in employees:
        table.insert("", 'end', values=employee)

    scrollbar = ttk.Scrollbar(win6, orient='vertical', command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

def btn_manager_task():
    #Выводит задания
    global win7
    win7 = tk.Toplevel()
    win7.title('Задания')
    win7.config(bg='#282828')
    win7.geometry('1420x600')

    cursor.execute("select count(*) from actions;")
    rows = cursor.fetchall
    cursor.execute("select * from actions;")
    employees = cursor.fetchall()

    columns = ('order_id', 'employee_id', 'executor', 'creation_time', 'execution_time', 'end_time', 'priority', 'status', 'action')

    table = ttk.Treeview(win7, columns=columns, show='headings', height=15)
    table.grid(row=0, column=0, sticky="nsew")
    table.heading('order_id', text='ID заказа')
    table.heading('employee_id', text='ID менеджера')
    table.heading('executor', text='ID работника')
    table.heading('creation_time', text='Время создания')
    table.heading('execution_time', text='Время исполения')
    table.heading('end_time', text='Срок')
    table.heading('priority', text='Приоритет')
    table.heading('status', text='Статус')
    table.heading('action', text='action')

    for employee in employees:
        table.insert("", 'end', values=employee)

    scrollbar = ttk.Scrollbar(win7, orient='vertical', command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

    scrollbar2 = ttk.Scrollbar(win7, orient='horizontal', command=table.xview)
    scrollbar2.grid(row=1, column=0, sticky='we')
    table.configure(xscrollcommand=scrollbar2.set)

def btn_create():
    #Создает задание
    global win8
    win8 = tk.Toplevel()
    win8.title('Задания')
    win8.config(bg='#282828')
    win8.geometry('375x365')
    win8.resizable(False, False)

    label_order_id = tk.Label(win8, text='ID заказа:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=0, column=0, sticky='e')
    label_employee_id = tk.Label(win8, text='ID менеджера:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=1, column=0, sticky='e')
    label_executor = tk.Label(win8, text='ID работника:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=2, column=0, sticky='e') 
    label_execution_time = tk.Label(win8, text='Время исполнения:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=3, column=0, sticky='e') 
    label_end_time = tk.Label(win8, text='Срок:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=4, column=0, sticky='e') 
    label_priority = tk.Label(win8, text='Приоритет:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=5, column=0, sticky='e')  
    label_action = tk.Label(win8, text='action:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
        row=6, column=0, sticky='e') 

    global entry_order_id, entry_employee_id, entry_executor, entry_execution_time, entry_end_time, entry_priority, entry_action

    entry_order_id = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_employee_id = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_executor = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_execution_time = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_end_time = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_priority = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))
    entry_action = tk.Entry(win8, bg='#282828', fg='white', font=('Calibri Light', 14))

    entry_order_id.grid(row=0, column=1)
    entry_employee_id.grid(row=1, column=1)
    entry_executor.grid(row=2, column=1)
    entry_execution_time.grid(row=3, column=1)
    entry_end_time.grid(row=4, column=1)
    entry_priority.grid(row=5, column=1)
    entry_action.grid(row=6, column=1)

    button_5 = tk.Button(win8, text='Ок',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_5Click, width=10).grid(
        row=7, column=1, sticky='e')

def btn_5Click():
    #Заполлнение action
    global cursor
    #Получаем информацию с Entry
    if (entry_order_id.get != None and entry_employee_id.get != None and entry_executor.get != None and entry_execution_time.get != None and entry_end_time.get != None, entry_priority.get != None, entry_action.get != None):
        cursor.execute(
            f"""insert into actions (order_id , employee_id, executor, creation_time, execution_time, end_time, action, priority, status)
        values ({int(entry_order_id.get)}, {int(entry_employee_id.get)}, {int(entry_executor.get)}, {datetime.now()}, {entry_execution_time.get}, {entry_end_time.get} ,'{entry_action.get}', '{entry_priority}', true);"""
        )
        print('create')

def btn_empl_ot():
    #Отчет по сотрудникам
    cursor.execute("SELECT save_report_to_json_empl();")
    success_window = tk.Toplevel()
    success_window.geometry('300x100')
    success_window.config(bg='#282828')
    tk.Label(success_window, text='Отчет по сотрудникам сохранен', bg='#282828', fg='white', font=('Calibri Light', 14)).pack()

def btn_task_ot():
    #Отчет по задачам
    cursor.execute("SELECT save_report_to_json();")
    success_window = tk.Toplevel()
    success_window.geometry('300x100')
    success_window.config(bg='#282828')
    tk.Label(success_window, text='Отчет по задачам сохранен', bg='#282828', fg='white', font=('Calibri Light', 14)).pack()

def button_em_task_click():
    #Задачи сотрудника
    global win9
    win9 = tk.Toplevel()
    win9.title('Задачи')
    win9.config(bg='#282828')
    win9.geometry('500x700')

    cursor.execute("select order_date_time, description from orders")
    employees = cursor.fetchall()

    columns = ('order_date_time', 'description')

    table = ttk.Treeview(win9, columns=columns, show='headings', height=400)
    table.grid(row=0, column=0, sticky="nsew")
    table.heading('order_date_time', text='Дата')
    table.heading('description', text='Описание')

    for employee in employees:
        table.insert("", 'end', values=employee)

    scrollbar = ttk.Scrollbar(win9, orient='vertical', command=table.yview)
    table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky="ns")

def btn_1Click():
    k = 2
    if (k == 1):
        employee()
    else:
        manager()

def on_closing1():
    win.deiconify()
    win3.destroy()

def on_closing2():
    win.deiconify()
    win2.destroy()

def on_closing3():
    win.deiconify()
    win4.destroy()

#Окно входа
win = tk.Tk()
win.title('pr7-8')
win.geometry('277x160+100+100')
win.config(bg='#282828')
win.resizable(False, False)

label_1 = tk.Label(win, text='Авторизация',bg='#282828', fg='white', font=('Calibri Light', 14), pady=5).grid(
    row=0, column=0, columnspan=2, stick='we')
label_2 = tk.Label(win, text='Логин:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
    row=1, column=0)
label_3 = tk.Label(win, text='Пароль:',bg='#282828', fg='white', font=('Calibri Light', 14), pady=7).grid(
    row=2, column= 0)

btn_1 = tk.Button(win, text='Вход',bg='#282828', fg='white', font=('Calibri Light', 14), activebackground='#181818',activeforeground='white', command=btn_1Click).grid(
    row=3, column=1, sticky='e')
btn_2 = tk.Button(win, text='Регистрация',bg='#282828', fg='white', font=('Calibri Light', 12),activebackground='#181818',activeforeground='white', command=btn_2Click).grid(
    row=3, column=0, sticky='w', columnspan=2)

login = tk.Entry(win, bg='#282828', fg='white', font=('Calibri Light', 14)).grid(
    row = 1, column=1)
password = tk.Entry(win, bg='#282828', fg='white', font=('Calibri Light', 14), show = '*').grid(
    row=2, column=1)

win.mainloop()