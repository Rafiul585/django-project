from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.


def index(request):

    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')

        if emp_id != '' and full_name != '' and email != '':
            Employee.objects.create(
                emp_id=emp_id, emp_name=full_name, emp_email=email)
            return redirect('/show')

    return render(request, 'employee_app/index.html')


def show(request):
    context = {
        'employees': Employee.objects.all()
    }
    return render(request, 'employee_app/show.html', context)


def edit(request, id):
    print("7777777777777777777",id)
    employee_info = Employee.objects.get(id=id)
    return render(request, 'employee_app/edit.html', context={'employee_info': employee_info})