from django.contrib import admin
from .models import Client, Employee, Item, WorkType, ServiceCost

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Item)
admin.site.register(WorkType)
admin.site.register(ServiceCost)
