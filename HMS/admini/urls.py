from django.urls import path
from .import views



urlpatterns = [

   
    path('index', views.index, name="index"),

    

    
    #HIZI NI KWA AJILI YA WAZEE
    

    #MWISHO WA YOTE NI HAPA

    path('all_time_payment/', views.all_time_payment, name="all_time_payment"),
    path('today_payment/', views.today_payment, name="today_payment"),
    path('add_available_medicines/', views.add_available_medicines.as_view(), name="add_available_medicines"),
    path('update_available_medicines/<int:pk>/', views.update_available_medicines.as_view(), name="update_available_medicines"),
    path('delete_available_medicines/<int:pk>/', views.delete_available_medicines, name="delete_available_medicines"),
    
    path('search_available_medicines/', views.search_available_medicines, name="search_available_medicines"),
 
]