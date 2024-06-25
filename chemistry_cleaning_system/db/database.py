import sqlite3

class Database:
    def __init__(self, db_name='dry_cleaning.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        self.seed_data()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS services (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    cost REAL NOT NULL)''')

            self.conn.execute('''CREATE TABLE IF NOT EXISTS employees (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    position TEXT NOT NULL)''')

            self.conn.execute('''CREATE TABLE IF NOT EXISTS clients (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    phone TEXT NOT NULL)''')

            self.conn.execute('''CREATE TABLE IF NOT EXISTS items (
                                    id INTEGER PRIMARY KEY,
                                    description TEXT NOT NULL,
                                    client_id INTEGER,
                                    service_id INTEGER,
                                    FOREIGN KEY(client_id) REFERENCES clients(id),
                                    FOREIGN KEY(service_id) REFERENCES services(id))''')

    def seed_data(self):
        with self.conn:
            cursor = self.conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM services")
            if cursor.fetchone()[0] == 0:
                self.conn.execute("INSERT INTO services (name, cost) VALUES ('Стирка', 500.00)")
                self.conn.execute("INSERT INTO services (name, cost) VALUES ('Химчистка', 1000.00)")

            cursor.execute("SELECT COUNT(*) FROM employees")
            if cursor.fetchone()[0] == 0:
                self.conn.execute("INSERT INTO employees (name, position) VALUES ('Иван Иванов', 'Менеджер')")
                self.conn.execute("INSERT INTO employees (name, position) VALUES ('Мария Петрова', 'Работник')")

            cursor.execute("SELECT COUNT(*) FROM clients")
            if cursor.fetchone()[0] == 0:
                self.conn.execute("INSERT INTO clients (name, phone) VALUES ('Алексей Сидоров', '+71234567890')")
                self.conn.execute("INSERT INTO clients (name, phone) VALUES ('Наталья Смирнова', '+79876543210')")

            cursor.execute("SELECT COUNT(*) FROM items")
            if cursor.fetchone()[0] == 0:
                self.conn.execute("INSERT INTO items (description, client_id, service_id) VALUES ('Пальто', 1, 2)")
                self.conn.execute("INSERT INTO items (description, client_id, service_id) VALUES ('Куртка', 2, 1)")

    def insert_service(self, name, cost):
        with self.conn:
            self.conn.execute("INSERT INTO services (name, cost) VALUES (?, ?)", (name, cost))

    def insert_employee(self, name, position):
        with self.conn:
            self.conn.execute("INSERT INTO employees (name, position) VALUES (?, ?)", (name, position))

    def insert_client(self, name, phone):
        with self.conn:
            self.conn.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))

    def insert_item(self, description, client_id, service_id):
        with self.conn:
            self.conn.execute("INSERT INTO items (description, client_id, service_id) VALUES (?, ?, ?)",
                              (description, client_id, service_id))

    def update_service(self, service_id, name, cost):
        with self.conn:
            self.conn.execute("UPDATE services SET name = ?, cost = ? WHERE id = ?", (name, cost, service_id))

    def update_employee(self, employee_id, name, position):
        with self.conn:
            self.conn.execute("UPDATE employees SET name = ?, position = ? WHERE id = ?", (name, position, employee_id))

    def update_client(self, client_id, name, phone):
        with self.conn:
            self.conn.execute("UPDATE clients SET name = ?, phone = ? WHERE id = ?", (name, phone, client_id))

    def update_item(self, item_id, description, client_id, service_id):
        with self.conn:
            self.conn.execute("UPDATE items SET description = ?, client_id = ?, service_id = ? WHERE id = ?", 
                              (description, client_id, service_id, item_id))

    def delete_service(self, service_id):
        with self.conn:
            self.conn.execute("DELETE FROM services WHERE id = ?", (service_id,))

    def delete_employee(self, employee_id):
        with self.conn:
            self.conn.execute("DELETE FROM employees WHERE id = ?", (employee_id,))

    def delete_client(self, client_id):
        with self.conn:
            self.conn.execute("DELETE FROM clients WHERE id = ?", (client_id,))

    def delete_item(self, item_id):
        with self.conn:
            self.conn.execute("DELETE FROM items WHERE id = ?", (item_id,))

    def get_services(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM services").fetchall()

    def get_employees(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM employees").fetchall()

    def get_clients(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM clients").fetchall()

    def get_items(self):
        with self.conn:
            return self.conn.execute("SELECT * FROM items").fetchall()
