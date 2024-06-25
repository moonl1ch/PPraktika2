import tkinter as tk
from tkinter import ttk

class AddServiceForm:
    def __init__(self, root, db, table):
        self.root = tk.Toplevel(root)
        self.root.title("Добавить услугу")
        self.db = db
        self.table = table
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Название").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Стоимость").grid(row=1, column=0, padx=10, pady=10)
        self.cost_entry = ttk.Entry(self.root)
        self.cost_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Сохранить", command=self.save_service).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_service(self):
        name = self.name_entry.get()
        cost = self.cost_entry.get()
        self.db.insert_service(name, cost)
        self.table.update_table()
        self.root.destroy()

class AddEmployeeForm:
    def __init__(self, root, db, table):
        self.root = tk.Toplevel(root)
        self.root.title("Добавить сотрудника")
        self.db = db
        self.table = table
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Имя").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Должность").grid(row=1, column=0, padx=10, pady=10)
        self.position_entry = ttk.Entry(self.root)
        self.position_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Сохранить", command=self.save_employee).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_employee(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        self.db.insert_employee(name, position)
        self.table.update_table()
        self.root.destroy()

class AddClientForm:
    def __init__(self, root, db, table):
        self.root = tk.Toplevel(root)
        self.root.title("Добавить клиента")
        self.db = db
        self.table = table
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Имя").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Телефон").grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = ttk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Сохранить", command=self.save_client).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_client(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.db.insert_client(name, phone)
        self.table.update_table()
        self.root.destroy()

class AddItemForm:
    def __init__(self, root, db, table):
        self.root = tk.Toplevel(root)
        self.root.title("Добавить вещь")
        self.db = db
        self.table = table
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Описание").grid(row=0, column=0, padx=10, pady=10)
        self.description_entry = ttk.Entry(self.root)
        self.description_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Клиент ID").grid(row=1, column=0, padx=10, pady=10)
        self.client_id_entry = ttk.Entry(self.root)
        self.client_id_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Услуга ID").grid(row=2, column=0, padx=10, pady=10)
        self.service_id_entry = ttk.Entry(self.root)
        self.service_id_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Сохранить", command=self.save_item).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def save_item(self):
        description = self.description_entry.get()
        client_id = self.client_id_entry.get()
        service_id = self.service_id_entry.get()
        self.db.insert_item(description, client_id, service_id)
        self.table.update_table()
        self.root.destroy()
