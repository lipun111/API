from django.contrib import admin
from webapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id','eno','ename','esal','eaddr')
    list_display_links=('id','ename')

admin.site.register(Employee,EmployeeAdmin)
