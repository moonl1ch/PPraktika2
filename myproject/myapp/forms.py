from django import forms
from .models import Client, Employee, Item, WorkType, ServiceCost

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = '__all__'

class ServiceCostForm(forms.ModelForm):
    class Meta:
        model = ServiceCost
        fields = '__all__'
