import tkinter as tk
from tkinter import ttk
from ui.tables import ServicesTable, EmployeesTable, ClientsTable, ItemsTable
from ui.add_edit_forms import AddServiceForm, AddEmployeeForm, AddClientForm, AddItemForm
from db.database import Database
from export.to_word import WordExporter
from export.to_excel import ExcelExporter

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Информационная система «Химчистка»")
        self.root.geometry("1024x768")
        self.db = Database()
        
        self.create_widgets()
        self.word_exporter = WordExporter(self.db)
        self.excel_exporter = ExcelExporter(self.db)

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook.Tab', font=('Helvetica', 12, 'bold'), padding=[10, 10, 10, 10], background='#4CAF50')
        style.configure('TButton', font=('Helvetica', 12), padding=6, background='#4CAF50', foreground='white')
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'), background='#4CAF50', foreground='white')
        style.configure('Treeview', font=('Helvetica', 12), rowheight=25, background='white', fieldbackground='white')

        tab_control = ttk.Notebook(self.root)

        services_tab = ttk.Frame(tab_control)
        employees_tab = ttk.Frame(tab_control)
        clients_tab = ttk.Frame(tab_control)
        items_tab = ttk.Frame(tab_control)

        tab_control.add(services_tab, text='Услуги')
        tab_control.add(employees_tab, text='Сотрудники')
        tab_control.add(clients_tab, text='Клиенты')
        tab_control.add(items_tab, text='Вещи')

        tab_control.pack(expand=1, fill='both')

        self.services_table = ServicesTable(services_tab, self.db)
        self.employees_table = EmployeesTable(employees_tab, self.db)
        self.clients_table = ClientsTable(clients_tab, self.db)
        self.items_table = ItemsTable(items_tab, self.db)
        
        self.create_menus()

    def create_menus(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Выход", command=self.root.quit)

        add_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Добавить", menu=add_menu)
        add_menu.add_command(label="Услугу", command=self.open_add_service_form)
        add_menu.add_command(label="Сотрудника", command=self.open_add_employee_form)
        add_menu.add_command(label="Клиента", command=self.open_add_client_form)
        add_menu.add_command(label="Вещь", command=self.open_add_item_form)

        export_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Экспорт", menu=export_menu)
        export_menu.add_command(label="Экспортировать услуги в Word", command=self.export_services_to_word)
        export_menu.add_command(label="Экспортировать услуги в Excel", command=self.export_services_to_excel)
        export_menu.add_command(label="Экспортировать сотрудников в Word", command=self.export_employees_to_word)
        export_menu.add_command(label="Экспортировать сотрудников в Excel", command=self.export_employees_to_excel)
        export_menu.add_command(label="Экспортировать клиентов в Word", command=self.export_clients_to_word)
        export_menu.add_command(label="Экспортировать клиентов в Excel", command=self.export_clients_to_excel)
        export_menu.add_command(label="Экспортировать вещи в Word", command=self.export_items_to_word)
        export_menu.add_command(label="Экспортировать вещи в Excel", command=self.export_items_to_excel)
        export_menu.add_command(label="Экспортировать все данные в Word", command=self.export_all_to_word)
        export_menu.add_command(label="Экспортировать все данные в Excel", command=self.export_all_to_excel)

    def open_add_service_form(self):
        AddServiceForm(self.root, self.db, self.services_table)

    def open_add_employee_form(self):
        AddEmployeeForm(self.root, self.db, self.employees_table)

    def open_add_client_form(self):
        AddClientForm(self.root, self.db, self.clients_table)

    def open_add_item_form(self):
        AddItemForm(self.root, self.db, self.items_table)

    def export_services_to_word(self):
        self.word_exporter.export_services()

    def export_services_to_excel(self):
        self.excel_exporter.export_services()

    def export_employees_to_word(self):
        self.word_exporter.export_employees()

    def export_employees_to_excel(self):
        self.excel_exporter.export_employees()

    def export_clients_to_word(self):
        self.word_exporter.export_clients()

    def export_clients_to_excel(self):
        self.excel_exporter.export_clients()

    def export_items_to_word(self):
        self.word_exporter.export_items()

    def export_items_to_excel(self):
        self.excel_exporter.export_items()

    def export_all_to_word(self):
        self.word_exporter.export_all()

    def export_all_to_excel(self):
        self.excel_exporter.export_all()
