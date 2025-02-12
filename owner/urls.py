from django.urls import path
from owner import views

urlpatterns = [
    path("index/", views.index, name= "index"),
    path("jobs/", views.jobs, name="jobs"),
    path("", views.register, name="register"),   
    path('addjob/', views.addjob, name='addjob'),
    path('employees/', views.employee_list, name='employee'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/update/', views.update_employee, name='update_employee'),
    path('login/', views.login, name='login'),
    ]
