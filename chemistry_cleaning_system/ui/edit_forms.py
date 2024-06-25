import tkinter as tk
from tkinter import ttk

class EditServiceForm:
    def __init__(self, root, db, item_values, table):
        self.root = tk.Toplevel(root)
        self.root.title("Редактировать услугу")
        self.db = db
        self.service_id = item_values[0]
        self.table = table
        self.create_widgets(item_values)

    def create_widgets(self, item_values):
        ttk.Label(self.root, text="Название").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry.insert(0, item_values[1])

        ttk.Label(self.root, text="Стоимость").grid(row=1, column=0, padx=10, pady=10)
        self.cost_entry = ttk.Entry(self.root)
        self.cost_entry.grid(row=1, column=1, padx=10, pady=10)
        self.cost_entry.insert(0, item_values[2])

        ttk.Button(self.root, text="Сохранить", command=self.save_service).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_service(self):
        name = self.name_entry.get()
        cost = self.cost_entry.get()
        self.db.update_service(self.service_id, name, cost)
        self.table.update_table()
        self.root.destroy()

class EditEmployeeForm:
    def __init__(self, root, db, item_values, table):
        self.root = tk.Toplevel(root)
        self.root.title("Редактировать сотрудника")
        self.db = db
        self.employee_id = item_values[0]
        self.table = table
        self.create_widgets(item_values)

    def create_widgets(self, item_values):
        ttk.Label(self.root, text="Имя").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry.insert(0, item_values[1])

        ttk.Label(self.root, text="Должность").grid(row=1, column=0, padx=10, pady=10)
        self.position_entry = ttk.Entry(self.root)
        self.position_entry.grid(row=1, column=1, padx=10, pady=10)
        self.position_entry.insert(0, item_values[2])

        ttk.Button(self.root, text="Сохранить", command=self.save_employee).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_employee(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        self.db.update_employee(self.employee_id, name, position)
        self.table.update_table()
        self.root.destroy()

class EditClientForm:
    def __init__(self, root, db, item_values, table):
        self.root = tk.Toplevel(root)
        self.root.title("Редактировать клиента")
        self.db = db
        self.client_id = item_values[0]
        self.table = table
        self.create_widgets(item_values)

    def create_widgets(self, item_values):
        ttk.Label(self.root, text="Имя").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.name_entry.insert(0, item_values[1])

        ttk.Label(self.root, text="Телефон").grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = ttk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        self.phone_entry.insert(0, item_values[2])

        ttk.Button(self.root, text="Сохранить", command=self.save_client).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def save_client(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.db.update_client(self.client_id, name, phone)
        self.table.update_table()
        self.root.destroy()

class EditItemForm:
    def __init__(self, root, db, item_values, table):
        self.root = tk.Toplevel(root)
        self.root.title("Редактировать вещь")
        self.db = db
        self.item_id = item_values[0]
        self.table = table
        self.create_widgets(item_values)

    def create_widgets(self, item_values):
        ttk.Label(self.root, text="Описание").grid(row=0, column=0, padx=10, pady=10)
        self.description_entry = ttk.Entry(self.root)
        self.description_entry.grid(row=0, column=1, padx=10, pady=10)
        self.description_entry.insert(0, item_values[1])

        ttk.Label(self.root, text="Клиент ID").grid(row=1, column=0, padx=10, pady=10)
        self.client_id_entry = ttk.Entry(self.root)
        self.client_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.client_id_entry.insert(0, item_values[2])

        ttk.Label(self.root, text="Услуга ID").grid(row=2, column=0, padx=10, pady=10)
        self.service_id_entry = ttk.Entry(self.root)
        self.service_id_entry.grid(row=2, column=1, padx=10, pady=10)
        self.service_id_entry.insert(0, item_values[3])

        ttk.Button(self.root, text="Сохранить", command=self.save_item).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def save_item(self):
        description = self.description_entry.get()
        client_id = self.client_id_entry.get()
        service_id = self.service_id_entry.get()
        self.db.update_item(self.item_id, description, client_id, service_id)
        self.table.update_table()
        self.root.destroy()
