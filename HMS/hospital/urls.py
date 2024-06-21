from django.urls import path
from .import views



urlpatterns = [

   
    path('home/', views.home, name="home"),
    path('Clinic_services_Categories_Page/', views.Clinic_services_Categories_Page, name="Clinic_services_Categories_Page"),
    path('Clinic_services_Page/<int:id>/', views.Clinic_services_Page, name="Clinic_services_Page"),
    path('search_clinic_service_autocomplete/', views.search_clinic_service_autocomplete, name="search_clinic_service_autocomplete"),
   
    path('base/', views.base.as_view(), name="base"),
    path('PatientCategoriesPage/', views.PatientCategoriesPage, name="PatientCategoriesPage"),
    path('uchafu/', views.uchafu, name="uchafu"),
    path('daily_amount/', views.daily_amount, name="daily_amount"),
    path('search_tribe/', views.search_tribe, name="search_tribe"),
    path('search_Pharmarcist_Comments/', views.search_Pharmarcist_Comments, name="search_Pharmarcist_Comments"),
    path('search_Pharmarcist_Comments_vipimo/', views.search_Pharmarcist_Comments_vipimo, name="search_Pharmarcist_Comments_vipimo"),
    path('search_Saved_patient_autocomplete/', views.search_Saved_patient_autocomplete, name="search_Saved_patient_autocomplete"),
    path('search_clinic_service/', views.search_clinic_service, name="search_clinic_service"),
    path('print_patient_details/<int:id>/', views.print_patient_details, name="print_patient_details"),
    

    path('print_detail_watoto_vipimo/<int:id>/', views.print_detail_watoto_vipimo, name="print_detail_watoto_vipimo"),
    








    path('services/', views.services, name="services"),
    path('patients/', views.patients, name="patients"),
    path('list_of_dozi_vipimo/', views.list_of_dozi_vipimo, name="list_of_dozi_vipimo"),
    path('doctors/', views.doctors, name="doctors"),
    path('PatientRegistration/', views.PatientRegistration.as_view(), name="PatientRegistration"),
    path('PatientRegistration_list/<int:id>/', views.PatientRegistration_list, name="PatientRegistration_list"),
    path('SavedPatients_list/', views.SavedPatients_list, name="SavedPatients_list"),
    path('SavedPatients_list_Vipimo/', views.SavedPatients_list_Vipimo, name="SavedPatients_list_Vipimo"),
    path('DoctorServicesCategory/', views.DoctorServicesCategory, name="DoctorServicesCategory"),
    
    path('UpdateRegisteredPatients/<int:pk>/', views.UpdateRegisteredPatients.as_view(), name="UpdateRegisteredPatients"),
    path('DeleteRegisteredPatients/<int:pk>/', views.DeleteRegisteredPatients, name="DeleteRegisteredPatients"),
    #path('watoto_detail/<int:pk>/', views.watoto_detail.as_view(), name="watoto_detail"),


    #URL KWA AJILI YA DOZI ZINAANZIA HAPA
    path('add_dozi/', views.add_dozi, name="add_dozi"),
    path('list_dozi/', views.list_dozi, name="list_dozi"),
    path('dozi_update/<int:pk>/', views.dozi_update, name="dozi_update"),
    path('dozi_delete/<int:pk>/', views.dozi_delete, name="dozi_delete"),
    
    path('search_kipimo/', views.search_kipimo, name="search_kipimo"),
    path('search_mtoto/', views.search_mtoto, name="search_mtoto"),
    path('search_MyUsers_autocomplete/', views.search_MyUsers_autocomplete, name="search_MyUsers_autocomplete"),
    
    
    #path('dozi_update_quantity/<int:pk>/', views.dozi_update_quantity, name="dozi_update_quantity"),
    path('add_quantity/<int:id>/', views.add_quantity, name="add_quantity"),
    path('accept_medicine/<int:id>/', views.accept_medicine, name="accept_medicine"),
     #URL KWA AJILI YA DOZI ZINZISHIA HAPA



    
#HIZI URL NI KWA AJILI YA VIPIMO ZINAANZIA HAPA
    path('add_kipimo/', views.add_kipimo, name="add_kipimo"),
    path('list_kipimo/', views.list_kipimo, name="list_kipimo"),
    path('kipimo_update/<int:pk>/', views.kipimo_update, name="kipimo_update"),
    path('kipimo_delete/<int:pk>/', views.kipimo_delete, name="kipimo_delete"),
    path('add_dawa/<int:id>/', views.add_dawa, name="add_dawa"),
    path('accept_vipimo/<int:id>/', views.accept_vipimo, name="accept_vipimo"),
    path('search_kipimo2/', views.search_kipimo2, name="search_kipimo2"),

 #URL KWA AJILI YA VIPIMO ZINZISHIA HAPA

  
    

     

    
    
 
    
 
]