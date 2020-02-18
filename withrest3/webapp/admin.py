from django.contrib import admin
from webapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','ename','eno','esal', 'eaddr']

admin.site.register(Employee,EmployeeAdmin)
