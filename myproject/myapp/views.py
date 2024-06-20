from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Employee, Item, WorkType, ServiceCost
from .forms import ClientForm, EmployeeForm, ItemForm, WorkTypeForm, ServiceCostForm
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')


# List views
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'myapp/client_list.html', {'clients': clients})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'myapp/employee_list.html', {'employees': employees})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})

def worktype_list(request):
    worktypes = WorkType.objects.all()
    return render(request, 'myapp/worktype_list.html', {'worktypes': worktypes})

def servicecost_list(request):
    servicecosts = ServiceCost.objects.all()
    return render(request, 'myapp/servicecost_list.html', {'servicecosts': servicecosts})

# Create views
def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'myapp/client_form.html', {'form': form})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'myapp/employee_form.html', {'form': form})

def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_form.html', {'form': form})

def worktype_create(request):
    if request.method == "POST":
        form = WorkTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('worktype_list')
    else:
        form = WorkTypeForm()
    return render(request, 'myapp/worktype_form.html', {'form': form})

def servicecost_create(request):
    if request.method == "POST":
        form = ServiceCostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicecost_list')
    else:
        form = ServiceCostForm()
    return render(request, 'myapp/servicecost_form.html', {'form': form})

# Update views
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'myapp/client_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'myapp/employee_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'myapp/item_form.html', {'form': form})

def worktype_update(request, pk):
    worktype = get_object_or_404(WorkType, pk=pk)
    if request.method == "POST":
        form = WorkTypeForm(request.POST, request.FILES, instance=worktype)
        if form.is_valid():
            form.save()
            return redirect('worktype_list')
    else:
        form = WorkTypeForm(instance=worktype)
    return render(request, 'myapp/worktype_form.html', {'form': form})

def servicecost_update(request, pk):
    servicecost = get_object_or_404(ServiceCost, pk=pk)
    if request.method == "POST":
        form = ServiceCostForm(request.POST, instance=servicecost)
        if form.is_valid():
            form.save()
            return redirect('servicecost_list')
    else:
        form = ServiceCostForm(instance=servicecost)
    return render(request, 'myapp/servicecost_form.html', {'form': form})

# Delete views
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'myapp/client_confirm_delete.html', {'client': client})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'myapp/employee_confirm_delete.html', {'employee': employee})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})

def worktype_delete(request, pk):
    worktype = get_object_or_404(WorkType, pk=pk)
    if request.method == "POST":
        worktype.delete()
        return redirect('worktype_list')
    return render(request, 'myapp/worktype_confirm_delete.html', {'worktype': worktype})

def servicecost_delete(request, pk):
    servicecost = get_object_or_404(ServiceCost, pk=pk)
    if request.method == "POST":
        servicecost.delete()
        return redirect('servicecost_list')
    return render(request, 'myapp/servicecost_confirm_delete.html', {'servicecost': servicecost})
