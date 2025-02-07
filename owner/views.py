from django.shortcuts import render


def register(request):
    return render(request, 'owner/register.html')

def login(request):
    return render(request, 'owner/login.html')

def index(request):
    return render(request, 'owner/index.html')


def jobs(request):
     return render(request, 'owner/job.html')

def addjob(request):
      return render(request, 'owner/addjob.html')


def employee_list(request):
        return render(request, "employee/employee.html")


def add_employee(request):
    return render(request, "employee/addemployee.html")


def update_employee(request):
    return render(request, "employee/updateemployee.html")



