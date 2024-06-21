#from hospital.forms import InvoiceForm
from django.contrib import admin
from hospital.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from hospital.forms import *


# Register your models here.
class MyUserAdmin(BaseUserAdmin):
    list_display=('first_name', 'middle_name', 'last_name', 'email', 'company_name', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_doctor', 'is_accountancy')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','username', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)

class ClinicServicesAdmin(admin.ModelAdmin):
    list_display=('ServiceName', 'ServicePrice')
    #form = DoziForm
    search_fields=('ServiceName',)
    
class ClinicServicesCategoriesAdmin(admin.ModelAdmin):
    list_display=('CategoryName',)
    #form = DoziForm
    search_fields=('CategoryName',)  
    

class DoziAdmin(admin.ModelAdmin):
    list_display=('name', 'total','TakenBy','huduma','paid', 'time_stamp')
    #form = DoziForm
    search_fields=('name',)
    
    
    list_filter=('huduma', 'time_stamp', 'paid','TakenBy', )

class VipimoAdmin(admin.ModelAdmin):
    list_display=('name', 'total', 'time_stamp')
    form = VipimoForm
    search_fields=('name',)
    
    
    list_filter=('name',)


class RegisteredPatientsAdmin(admin.ModelAdmin):
    list_display=('fname', 'sname', 'tname', 'reg_no', 'Category')
    form = PatientRegistrationForm
    search_fields=('fname', 'sname', 'tname', 'reg_no')
    list_filter=('Category',)








class AvailableMedicinesAdmin(admin.ModelAdmin):
    list_display=('medicine_name', 'quantity', 'price', 'created')
    form = AvailableMedicinesForm
    search_fields=('medicine_name',)
    
    
    list_filter=('medicine_name',)
    
    
    


admin.site.register(ClinicServices, ClinicServicesAdmin)
admin.site.register(ClinicServicesCategories, ClinicServicesCategoriesAdmin)

admin.site.register(Doctors)
admin.site.register(Tribe)



admin.site.register(RegisteredPatients, RegisteredPatientsAdmin)

# admin.site.register(Medicine)
admin.site.register(MyUser, MyUserAdmin)
#admin.site.register(Dozi)
admin.site.register(Dozi, DoziAdmin)
admin.site.register(Vipimo, VipimoAdmin)

admin.site.register(AvailableMedicines, AvailableMedicinesAdmin)
admin.site.register(PatientCategories)

