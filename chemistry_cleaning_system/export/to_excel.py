import xlsxwriter
from db.database import Database

class ExcelExporter:
    def __init__(self, db):
        self.db = db

    def export_services(self, filename='services.xlsx'):
        services = self.db.get_services()
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet('Услуги')

        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Название')
        worksheet.write(0, 2, 'Стоимость')

        for i, service in enumerate(services, start=1):
            worksheet.write(i, 0, service[0])
            worksheet.write(i, 1, service[1])
            worksheet.write(i, 2, service[2])

        workbook.close()

    def export_employees(self, filename='employees.xlsx'):
        employees = self.db.get_employees()
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet('Сотрудники')

        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Имя')
        worksheet.write(0, 2, 'Должность')

        for i, employee in enumerate(employees, start=1):
            worksheet.write(i, 0, employee[0])
            worksheet.write(i, 1, employee[1])
            worksheet.write(i, 2, employee[2])

        workbook.close()

    def export_clients(self, filename='clients.xlsx'):
        clients = self.db.get_clients()
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet('Клиенты')

        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Имя')
        worksheet.write(0, 2, 'Телефон')

        for i, client in enumerate(clients, start=1):
            worksheet.write(i, 0, client[0])
            worksheet.write(i, 1, client[1])
            worksheet.write(i, 2, client[2])

        workbook.close()

    def export_items(self, filename='items.xlsx'):
        items = self.db.get_items()
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet('Вещи')

        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Описание')
        worksheet.write(0, 2, 'Клиент ID')
        worksheet.write(0, 3, 'Услуга ID')

        for i, item in enumerate(items, start=1):
            worksheet.write(i, 0, item[0])
            worksheet.write(i, 1, item[1])
            worksheet.write(i, 2, item[2])
            worksheet.write(i, 3, item[3])

        workbook.close()

    def export_all(self, filename='all_data.xlsx'):
        services = self.db.get_services()
        employees = self.db.get_employees()
        clients = self.db.get_clients()
        items = self.db.get_items()

        workbook = xlsxwriter.Workbook(filename)

        worksheet = workbook.add_worksheet('Услуги')
        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Название')
        worksheet.write(0, 2, 'Стоимость')
        for i, service in enumerate(services, start=1):
            worksheet.write(i, 0, service[0])
            worksheet.write(i, 1, service[1])
            worksheet.write(i, 2, service[2])

        worksheet = workbook.add_worksheet('Сотрудники')
        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Имя')
        worksheet.write(0, 2, 'Должность')
        for i, employee in enumerate(employees, start=1):
            worksheet.write(i, 0, employee[0])
            worksheet.write(i, 1, employee[1])
            worksheet.write(i, 2, employee[2])

        worksheet = workbook.add_worksheet('Клиенты')
        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Имя')
        worksheet.write(0, 2, 'Телефон')
        for i, client in enumerate(clients, start=1):
            worksheet.write(i, 0, client[0])
            worksheet.write(i, 1, client[1])
            worksheet.write(i, 2, client[2])

        worksheet = workbook.add_worksheet('Вещи')
        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Описание')
        worksheet.write(0, 2, 'Клиент ID')
        worksheet.write(0, 3, 'Услуга ID')
        for i, item in enumerate(items, start=1):
            worksheet.write(i, 0, item[0])
            worksheet.write(i, 1, item[1])
            worksheet.write(i, 2, item[2])
            worksheet.write(i, 3, item[3])

        workbook.close()
