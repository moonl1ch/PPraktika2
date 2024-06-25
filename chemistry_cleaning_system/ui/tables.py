import tkinter as tk
from tkinter import ttk
from ui.edit_forms import EditServiceForm, EditEmployeeForm, EditClientForm, EditItemForm

class ServicesTable:
    def __init__(self, root, db):
        self.db = db
        self.tree = ttk.Treeview(root, columns=('ID', 'Название', 'Стоимость'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Название', text='Название')
        self.tree.heading('Стоимость', text='Стоимость')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind('<Delete>', self.delete_selected)
        self.tree.bind('<Double-1>', self.edit_selected)

        self.update_table()

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.db.get_services():
            self.tree.insert('', tk.END, values=row)

    def delete_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_id = self.tree.item(selected_item)['values'][0]
        self.db.delete_service(item_id)
        self.update_table()

    def edit_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_values = self.tree.item(selected_item)['values']
        EditServiceForm(self.tree, self.db, item_values, self)

class EmployeesTable:
    def __init__(self, root, db):
        self.db = db
        self.tree = ttk.Treeview(root, columns=('ID', 'Имя', 'Должность'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Имя', text='Имя')
        self.tree.heading('Должность', text='Должность')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind('<Delete>', self.delete_selected)
        self.tree.bind('<Double-1>', self.edit_selected)

        self.update_table()

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.db.get_employees():
            self.tree.insert('', tk.END, values=row)

    def delete_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_id = self.tree.item(selected_item)['values'][0]
        self.db.delete_employee(item_id)
        self.update_table()

    def edit_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_values = self.tree.item(selected_item)['values']
        EditEmployeeForm(self.tree, self.db, item_values, self)

class ClientsTable:
    def __init__(self, root, db):
        self.db = db
        self.tree = ttk.Treeview(root, columns=('ID', 'Имя', 'Телефон'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Имя', text='Имя')
        self.tree.heading('Телефон', text='Телефон')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind('<Delete>', self.delete_selected)
        self.tree.bind('<Double-1>', self.edit_selected)

        self.update_table()

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.db.get_clients():
            self.tree.insert('', tk.END, values=row)

    def delete_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_id = self.tree.item(selected_item)['values'][0]
        self.db.delete_client(item_id)
        self.update_table()

    def edit_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_values = self.tree.item(selected_item)['values']
        EditClientForm(self.tree, self.db, item_values, self)

class ItemsTable:
    def __init__(self, root, db):
        self.db = db
        self.tree = ttk.Treeview(root, columns=('ID', 'Описание', 'Клиент ID', 'Услуга ID'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Описание', text='Описание')
        self.tree.heading('Клиент ID', text='Клиент ID')
        self.tree.heading('Услуга ID', text='Услуга ID')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind('<Delete>', self.delete_selected)
        self.tree.bind('<Double-1>', self.edit_selected)

        self.update_table()

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.db.get_items():
            self.tree.insert('', tk.END, values=row)

    def delete_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_id = self.tree.item(selected_item)['values'][0]
        self.db.delete_item(item_id)
        self.update_table()

    def edit_selected(self, event):
        selected_item = self.tree.selection()[0]
        item_values = self.tree.item(selected_item)['values']
        EditItemForm(self.tree, self.db, item_values, self)
