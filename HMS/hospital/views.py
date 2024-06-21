
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from hospital.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from hospital.forms import * 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import calendar
from calendar import HTMLCalendar
from django.utils import timezone
from django.db.models import Sum, Max, Min, Avg
from django.core.files.base import ContentFile

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders




import datetime

import csv


# Create your views here.
def Clinic_services_Categories_Page(request):
    #title = 'List of Vipimo'
    category = ClinicServicesCategories.objects.all().order_by('id')

    paginator = Paginator(category, 2)  # Show 6 contacts per page
    page = request.GET.get('page')
    category = paginator.get_page(page)
    
    
    context = {
        
        
        "category":category
    }

    return render(request, 'hospital/Clinic_services_Categories_Page.html', context)


def Clinic_services_Page(request,id):
    category = ClinicServicesCategories.objects.get(id=id)
    categoryId_id = category.id
    categoryId_name = category.CategoryName
    #title = 'List of Vipimo'
    services = ClinicServices.objects.filter(
            Category__id__icontains=categoryId_id

        )
    form = ClinicServicesSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    #searching button codes
    if request.method == 'POST':
        services = ClinicServices.objects.filter( 
            ServiceName__icontains=form['ServiceName'].value()
        )

    paginator = Paginator(services, 10)  # Show 6 contacts per page
    page = request.GET.get('page')
    services = paginator.get_page(page)

    context = {
        "form":form,
        "categoryId_name":categoryId_name,
        
        "services":services
    }

    return render(request, 'hospital/Clinic_services_Page.html', context)


def search_clinic_service_autocomplete(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(ServiceName__contains=query_original)
        #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = ClinicServices.objects.filter(search)
    mylist= []
    mylist += [x.ServiceName  for x in queryseti]

    return JsonResponse(mylist, safe=False)





def search_tribe(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(tribe_choices__contains=query_original)
        #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = Tribe.objects.filter(search)
    mylist= []
    mylist += [x.tribe  for x in queryseti]

    return JsonResponse(mylist, safe=False)

#CODES ZA KUPRINT DETAILS ZA WAGONJWA WENYE VIPIMO ZINAANZIA HAPA
def print_detail_watoto_vipimo(request, id):
    
    querySet = Vipimo.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        
   
    #return render(request, 'hospital/print_detail.html',context)


#CODES ZA KUPRINT DETAILS ZA WAGONJWA WENYE DOZI ZINAANZIA HAPA
def print_patient_details(request, id):
    
    querySet = Dozi.objects.get(id=id)
    template_path = 'hospital/print_detail.html'
    #querySet = KawaidaDozi.objects.get(id=id)
    context = {
        "querySet": querySet

    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    #if you want to download before opening it
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status= pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response

        

    #return render(request, 'hospital/print_detail.html',context)


    #HIZO CODES ZINAISHIA HAPA
  
    

class base(TemplateView):
    template_name = 'hospital/base.html'
   
 

def daily_amount(request):

    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        enddate = request.POST.get('enddate')

        result = KawaidaDozi.objects.raw('select id, name, time_stamp, total from KAWAIDA_DOZI where time_stamp between "'+fromdate+'" and "'+enddate+'" ')
        context = {
        
        "queryset":result,
        }
        
    
        return render(request, 'hospital/daily_amount.html', context)
    else:

        start_date = datetime.date(2021,10,13)
        end_date = datetime.date(2021,12,30)

        myDate = datetime.datetime.now()
        myDate1 = datetime.datetime.now().date()
        myDate2 = datetime.datetime.now().time()
       # formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
       #from django.utils import timezone

      #now = timezone.now()
        
        queryset = KawaidaDozi.objects.filter(time_stamp__range=(start_date, end_date))
        
        
        context = {
            
            "queryset":queryset,
            "myDate": myDate,
            "myDate1": myDate1,
            "myDate2": myDate2
            
        }
       

        return render(request, 'hospital/daily_amount.html', context)



def uchafu(request, year=datetime.datetime.now().year,month=datetime.datetime.now().strftime('%B')):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        enddate = request.POST.get('enddate')

        result = KawaidaDozi.objects.raw('select id, name, time_stamp, total from KAWAIDA_DOZI where time_stamp between "'+fromdate+'" and "'+enddate+'" ')
        context = {
        
        "queryset":result,
        }
        
    
        return render(request, 'hospital/daily_amount.html', context)
    else:
        name = "john"
        month = month.capitalize()

        month_number = list(calendar.month_name).index(month)
        month_number = int(month_number)

        cal = HTMLCalendar().formatmonth(
            year,
            month_number


            )
        now = datetime.datetime.now()
        current_year = now.year

        event_list = KawaidaDozi.objects.filter(
            time_stamp__year = year,
            time_stamp__month = month_number

            )

        time = now.strftime('%I:%M %p')

        

            
        context = {
            
            
            "event_list": event_list,
            "name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "time": time,
            
        }
           

        return render(request, 'hospital/uchafu.html', context)

   

    







def home(response):
    
    
    return render(response, 'hospital/home.html')

def services(response):
    
    return render(response, 'hospital/services.html')

def list_of_dozi_vipimo(response):
    
    return render(response, 'hospital/list_of_dozi_vipimo.html')

def patients(response):
    
    return render(response, 'hospital/patients.html')



def doctors(response):
    doct = Doctors.objects.all()
    context = {
        "doct":doct
        
    }
    
    return render(response, 'hospital/doctors.html',context)


def PatientCategoriesPage(request):
    #title = 'List of Vipimo'
    category = PatientCategories.objects.all().order_by('-id')

    paginator = Paginator(category, 2)  # Show 6 contacts per page
    page = request.GET.get('page')
    category = paginator.get_page(page)
    
    
    context = {
        
        
        "category":category
    }

    return render(request, 'hospital/PatientCategoriesPage.html', context)

    
class PatientRegistration(SuccessMessageMixin, CreateView):
    model = RegisteredPatients
    template_name = 'hospital/PatientRegistration.html'
    form_class = PatientRegistrationForm
    success_url = reverse_lazy('PatientRegistration')
    success_message = "Data Added Successfully"
    
def PatientRegistration_list(request,id):
    #all_polls = 0
    
    params=0
    search_term =0
    
    categoryId = PatientCategories.objects.get(id=id)
    categoryIdName = categoryId.CategoryName

    

    watoto = RegisteredPatients.objects.filter(
                Category__id__icontains = categoryId.id
                )

    search_term = ''
    if 'fname' in request.GET:
        watoto = watoto.order_by('fname')

    if 'created' in request.GET:
        watoto = watoto.order_by('-created')

    if 'created2' in request.GET:
        watoto = watoto.order_by('created')

    
    # if 'search' in request.GET:
    #     search_term = request.GET['search']
    #     watoto = RegisteredPatients.filter(text__icontains=search_term)

    paginator = Paginator(watoto, 10)  # Show 6 contacts per page
    page = request.GET.get('page')
    watoto = paginator.get_page(page)

    # get_dict_copy = request.GET.copy()
    # params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    # print(params)

    context = {
        'watoto': watoto,
        #'all_polls': all_polls,
        'params': params,
        'search_term': search_term,
        'categoryIdName':categoryIdName,

    }
    return render(request, 'hospital/PatientRegistration_list.html', context)

def DoctorServicesCategory(request):
    
    return render(request, 'hospital/DoctorServicesCategory.html')


def SavedPatients_list(request):
    #all_polls = 0
    
    params=0
    search_term =0
    
    #categoryId = Dozi.objects.all()
    

    

    queryset = Dozi.objects.filter(
            huduma__icontains="dawa",
            paid = True
        )

    main_total_price = queryset.aggregate(Sum('total'))['total__sum']
    print(main_total_price);
    get_sum = 0
    get_sum_filter_date = 0
    start_date = 0
    end_date = 0
    username = 0
    

    form = FilterDoziSearchForm(request.POST or None)

    search_term = ''
    if 'fname' in request.GET:
        queryset = queryset.order_by('name')

    if 'time_stamp' in request.GET:
        queryset = queryset.order_by('-time_stamp')

    if 'time_stamp2' in request.GET:
        queryset = queryset.order_by('time_stamp')
  
    paginator = Paginator(queryset, 10)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    

    context = {
        'queryset': queryset,
        #'all_polls': all_polls,
        'params': params,
        'search_term': search_term,

        "form": form,
        "page":page,
        "main_total_price":main_total_price,
        "get_sum":get_sum,
        "get_sum_filter_date":get_sum_filter_date,
        "start_date":start_date,
        "end_date":end_date,
        "username":username,
        
        

    }





    if request.method == "POST":
        #kwa ajili ya kufilter items and category ktk form
            
        #category__icontains=form['category'].value(),
        TakenBy = form['TakenBy'].value()
        startDate = form['start_date'].value()
        endDate = form['end_date'].value()

        

        if (TakenBy != '' and startDate == '' and endDate == ''):

            # selected_user = MyUser.objects.get(id=user)
            # username = selected_user.username
            #print(f"USERNAME : {username}")
            username = TakenBy
            print(f"USERNAME : {username}")




            
            queryset = Dozi.objects.filter(
                huduma__icontains="dawa",
                paid = True
            ).order_by('-id')
            queryset = queryset.filter(TakenBy=TakenBy)

            get_sum = queryset.filter(
                TakenBy=TakenBy
            ).aggregate(sum=Sum('total'))

            search_term = ''
            if 'fname' in request.GET:
                queryset = queryset.order_by('name')

            if 'time_stamp' in request.GET:
                queryset = queryset.order_by('-time_stamp')

            if 'time_stamp2' in request.GET:
                queryset = queryset.order_by('time_stamp')
          
            paginator = Paginator(queryset, 10)  # Show 6 contacts per page
            page = request.GET.get('page')
            queryset = paginator.get_page(page)



        if (TakenBy != '' and startDate != '' and endDate != ''):

            # selected_user = MyUser.objects.get(id=user)
            # username = selected_user.username
            #print(f"USERNAME : {username}")
            username = TakenBy
            print(f"USERNAME : {username}")

            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
            
            print(f"END DATE {end_date}")
            print(f"START DATE {start_date}")

            queryset = Dozi.objects.filter(
                huduma__icontains="dawa",
                paid = True
            ).order_by('-id')
            queryset = queryset.filter(
                TakenBy=TakenBy,
                time_stamp__gte=start_date, 
                time_stamp__lte=end_date,
                 huduma__icontains="dawa",
                 paid=True

                )



            get_sum = queryset.filter(
                TakenBy=TakenBy,
                time_stamp__gte=start_date, time_stamp__lte=end_date
            ).aggregate(sum=Sum('total'))


            search_term = ''
            if 'fname' in request.GET:
                queryset = queryset.order_by('name')

            if 'time_stamp' in request.GET:
                queryset = queryset.order_by('-time_stamp')

            if 'time_stamp2' in request.GET:
                queryset = queryset.order_by('time_stamp')
          
            paginator = Paginator(queryset, 10)  # Show 6 contacts per page
            page = request.GET.get('page')
            queryset = paginator.get_page(page)





        if (TakenBy == '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)

            print(f"END DATE {end_date}")
            print(f"START DATE {start_date}")

            queryset = Dozi.objects.filter(
                # created__range=[

                #     form['start_date'].value(),
                #     form['end_date'].value()

                # ]
                time_stamp__gte=start_date, 
                time_stamp__lte=end_date,
                 huduma__icontains="dawa",
                 paid=True


                                            #product_name__icontains=form['product_name'].value(),
                                            #product_second_name__icontains=form['product_second_name'].value()
                                            #last_updated__gte=form['start_date'].value(),
                                            # last_updated__lte=form['end_date'].value()
                                            #last_updated__range=[
                                                #form['start_date'].value(),
                                                #form['end_date'].value()
                                            #]
                )
            # start_date = request.POST.get('start_date')
            # end_date = request.POST.get('end_date')

            get_sum_filter_date = queryset.filter(
                time_stamp__gte=start_date, time_stamp__lte=end_date
                ).aggregate(sum=Sum('total'))




            search_term = ''
            if 'fname' in request.GET:
                queryset = queryset.order_by('name')

            if 'time_stamp' in request.GET:
                queryset = queryset.order_by('-time_stamp')

            if 'time_stamp2' in request.GET:
                queryset = queryset.order_by('time_stamp')
          
            paginator = Paginator(queryset, 10)  # Show 6 contacts per page
            page = request.GET.get('page')
            queryset = paginator.get_page(page)


    #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
    if form['export_to_CSV'].value() == True:
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = 'attachment; filename="Patients Details.csv"'
        writer = csv.writer(response)
        writer.writerow(['Patient Full Name','Service', 'Amount Paid', 'Paid Status','Attended date'])
        instance = queryset
        for x in queryset:
            writer.writerow([x.name,x.huduma,x.total, x.paid,x.time_stamp ])
        return response
        #ZINAISHIA HAPA ZA KUDOWNLOAD



    context = {
        'queryset': queryset,
        #'all_polls': all_polls,
        'params': params,
        'search_term': search_term,

        "form": form,
        "page":page,
        "main_total_price":main_total_price,
        "get_sum":get_sum,
        "get_sum_filter_date":get_sum_filter_date,
        "start_date":start_date,
        "end_date":end_date,
        "username":username,
        
        

    }

    


    return render(request, 'hospital/SavedPatients_list.html', context)



def SavedPatients_list_Vipimo(request):
    #all_polls = 0
    
    params=0
    search_term =0
    
    #categoryId = Dozi.objects.all()
    

    

    queryset = Dozi.objects.filter(
            huduma__icontains="vipimo",
            paid = True
        )

    main_total_price = queryset.aggregate(Sum('total'))['total__sum']
    print(main_total_price);
    get_sum = 0
    get_sum_filter_date = 0
    start_date = 0
    end_date = 0
    username = 0
    

    form = FilterDoziSearchForm(request.POST or None)

    search_term = ''
    if 'fname' in request.GET:
        queryset = queryset.order_by('name')

    if 'time_stamp' in request.GET:
        queryset = queryset.order_by('-time_stamp')

    if 'time_stamp2' in request.GET:
        queryset = queryset.order_by('time_stamp')
  
    paginator = Paginator(queryset, 10)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    

    context = {
        'queryset': queryset,
        #'all_polls': all_polls,
        'params': params,
        'search_term': search_term,

        "form": form,
        "page":page,
        "main_total_price":main_total_price,
        "get_sum":get_sum,
        "get_sum_filter_date":get_sum_filter_date,
        "start_date":start_date,
        "end_date":end_date,
        "username":username,
        
        

    }





    if request.method == "POST":
        #kwa ajili ya kufilter items and category ktk form
            
        #category__icontains=form['category'].value(),
        TakenBy = form['TakenBy'].value()
        startDate = form['start_date'].value()
        endDate = form['end_date'].value()

        

        if (TakenBy != '' and startDate == '' and endDate == ''):

            # selected_user = MyUser.objects.get(id=user)
            # username = selected_user.username
            #print(f"USERNAME : {username}")
            username = TakenBy
            print(f"USERNAME : {username}")




            
            queryset = Dozi.objects.filter(
                huduma__icontains="vipimo",
                paid = True
            ).order_by('-id')
            queryset = queryset.filter(TakenBy=TakenBy)

            get_sum = queryset.filter(
                TakenBy=TakenBy
            ).aggregate(sum=Sum('total'))

            search_term = ''
            if 'fname' in request.GET:
                queryset = queryset.order_by('name')

            if 'time_stamp' in request.GET:
                queryset = queryset.order_by('-time_stamp')

            if 'time_stamp2' in request.GET:
                queryset = queryset.order_by('time_stamp')
          
            paginator = Paginator(queryset, 10)  # Show 6 contacts per page
            page = request.GET.get('page')
            queryset = paginator.get_page(page)



        if (TakenBy != '' and startDate != '' and endDate != ''):

            # selected_user = MyUser.objects.get(id=user)
            # username = selected_user.username
            #print(f"USERNAME : {username}")
            username = TakenBy
            print(f"USERNAME : {username}")

            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
            
            print(f"END DATE {end_date}")
            print(f"START DATE {start_date}")

            queryset = Dozi.objects.filter(
                huduma__icontains="vipimo",
                paid = True
            ).order_by('-id')
            queryset = queryset.filter(
                TakenBy=TakenBy,
                time_stamp__gte=start_date, 
                time_stamp__lte=end_date,
                 huduma__icontains="vipimo"

                )



            get_sum = queryset.filter(
                TakenBy=TakenBy,
                time_stamp__gte=start_date, 
                time_stamp__lte=end_date,
                 huduma__icontains="vipimo"
            ).aggregate(sum=Sum('total'))


            search_term = ''
            if 'fname' in request.GET:
                queryset = queryset.order_by('name')

            if 'time_stamp' in request.GET:
                queryset = queryset.order_by('-time_stamp')

            if 'time_stamp2' in request.GET:
                queryset = queryset.order_by('time_stamp')
          
            paginator = Paginator(queryset, 10)  # Show 6 contacts per page
            page = request.GET.get('page')
            queryset = paginator.get_page(page)





        if (TakenBy == '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)

            print(f"END DATE {end_date}")
            print(f"START DATE {start_date}")

            queryset = Dozi.objects.filter(
                # created__range=[

                #     form['start_date'].value(),
                #     form['end_date'].value()

                # ]
                time_stamp__gte=start_date, 
                time_stamp__lte=end_date,
                 huduma__icontains="vipimo",
                 paid=True


                                            #product_name__icontains=form['product_name'].value(),
                                            #product_second_name__icontains=form['product_second_name'].value()
                                            #last_updated__gte=form['start_date'].value(),
                                            # last_updated__lte=form['end_date'].value()
                                            #last_updated__range=[
                                                #form['start_date'].value(),
                                                #form['end_date'].value()
                                            #]
                )
            # start_date = request.POST.get('start_date')
            # end_date = request.POST.get('end_date')

            get_sum_filter_date = queryset.filter(
                time_stamp__gte=start_date, 
                time_stamp__lte=end_date,
                 

                ).aggregate(sum=Sum('total'))




            search_term = ''
            if 'fname' in request.GET:
                queryset = queryset.order_by('name')

            if 'time_stamp' in request.GET:
                queryset = queryset.order_by('-time_stamp')

            if 'time_stamp2' in request.GET:
                queryset = queryset.order_by('time_stamp')
          
            paginator = Paginator(queryset, 10)  # Show 6 contacts per page
            page = request.GET.get('page')
            queryset = paginator.get_page(page)


    #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
    if form['export_to_CSV'].value() == True:
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = 'attachment; filename="Patients Details.csv"'
        writer = csv.writer(response)
        writer.writerow(['Patient Full Name','Service', 'Amount Paid', 'Paid Status','Attended date'])
        instance = queryset
        for x in queryset:
            writer.writerow([x.name,x.huduma,x.total, x.paid,x.time_stamp ])
        return response
        #ZINAISHIA HAPA ZA KUDOWNLOAD



    context = {
        'queryset': queryset,
        #'all_polls': all_polls,
        'params': params,
        'search_term': search_term,

        "form": form,
        "page":page,
        "main_total_price":main_total_price,
        "get_sum":get_sum,
        "get_sum_filter_date":get_sum_filter_date,
        "start_date":start_date,
        "end_date":end_date,
        "username":username,
        
        

    }

    


    return render(request, 'hospital/SavedPatients_list_Vipimo.html', context)


class UpdateRegisteredPatients(SuccessMessageMixin, UpdateView):
    model = RegisteredPatients
    template_name = 'hospital/PatientRegistration.html'
    form_class = PatientRegistrationForm
    success_url = reverse_lazy('PatientCategoriesPage')
    success_message = "Data Updated Successfully"

def DeleteRegisteredPatients(request, pk):
    watoto = get_object_or_404(RegisteredPatients, id=pk)
    watoto.delete()
    return redirect('PatientCategoriesPage')

def search_Pharmarcist_Comments(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(name__icontains=query)
        results=Dozi.objects.filter(
            mysearch,
            huduma="dawa",
            paid=True
        )
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'hospital/search_Pharmarcist_Comments.html',context)

def search_Pharmarcist_Comments_vipimo(request):
    
    query=None
    results=[]
    
    if request.method == "GET":
        query=request.GET.get("search")
        mysearch=Q(name__icontains=query)
        results=Dozi.objects.filter(
            mysearch,
            huduma="vipimo",
            paid=True
        )
    context={
        
        "query":query,
        "results":results
    }
    return render(request, 'hospital/search_Pharmarcist_Comments_vipimo.html',context)



def search_Saved_patient_autocomplete(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(
        name__contains=query_original,
        paid=True
    ) #|Q(reg_no__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = Dozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)

#HIZI VIEWS KWA AJILI YA DOZI ZA WATOTO ZINAANZIA HAPA
#KWA AJILI YA KUADD DOZI ZA WATOTO
def add_dozi(request):
    
    form = DoziForm(request.POST or None)
    total_dozi = Dozi.objects.count()
    queryset = Dozi.objects.all().order_by('-id')[:3]  #hii ni kwa recent dozi
    print("START")
    if form.is_valid():

        

        instance = form.save(commit=False)
        instance.TakenBy = request.user.username
        instance.save()
        messages.info(request, "Informations were added successfully")
        return redirect('list_dozi')
        print("WELL")

    # messages.info(request, "Error when adding new Informations")
    # return redirect('add_dozi')
    print("ERROR")

    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "queryset":queryset
    }
    return render(request, 'hospital/add_dozi.html', context)
#KWA AJILIYA KUDISPLAY DOZI ZA WATOTO
def list_dozi(request):
    title = 'List of Dozi'
    queryset = Dozi.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "queryset":queryset,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        queryset = Dozi.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "queryset":queryset
    }

    return render(request, 'hospital/list_dozi.html', context)
#KWA AJILI YA KUAPDATE DOZI ZA WATOTO
def dozi_update(request, pk):
    queryset = Dozi.objects.order_by('-id')[:2]

    querySet = Dozi.objects.get(id=pk)
    form = DoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = DoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('list_dozi')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_dozi.html', context)

#HII NI KWA AJILI YA KUADD QUANTITY KWA WATOTO KWENYE SINGLE DETAIL LIST .HTML
def add_quantity(request, id):
    queryset = Dozi.objects.order_by('-id')[:2]

    querySet = Dozi.objects.get(id=id)
    form = DoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = DoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('add_quantity',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail.html', context)

#HII NI KWA AJILI YA KUACCEPT MEDICINE KWA WATOTO KWENYE SINGLE DETAIL LIST .HTML
def accept_medicine(request, id):
    queryset = Dozi.objects.order_by('-id')[:2]

    querySet = Dozi.objects.get(id=id)
    form = DoziUpdateForm(instance=querySet)
    if request.method == "POST":
        form = DoziUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "Informations sent successfully")
            return redirect('accept_medicine',id)
        messages.add_message(request, messages.SUCCESS, " It fails to submit data")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_list_detail.html', context)

       

        
        
    
    
    


#HII NI KWA AJILI YA KUDELETE DOZI YAMTOTO KWENYE LIST DOZI.HTML
  
def dozi_delete(request, pk):
    watoto = get_object_or_404(Dozi, id=pk)
    watoto.delete()
    return redirect('list_dozi')

'''
def dozi_delete(request, pk):
    querySet = Dozi.objects.get(id=pk)
    
    if request.method == "POST":
        querySet.delete()
        
        return redirect('/list_dozi')
    
    
    return render(request, 'hospital/delete_dozi.html')
'''

'''
    
    





class C(SuccessMessageMixin, DeleteView):
    model = RegisteredPatients
    template_name = 'hospital/delete_watoto.html'
    
    success_url = reverse_lazy('PatientRegistration_list')
    success_message = "Data Deleted Successfully"


'''
#hii ya chin ni kwaajili ya kumsearch mtu kwenye dozi_list.htm----->
def search_kipimo(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = Dozi.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)


#hii ya chin ni kwaajili ya kumsearch mtoto kwenye add_dozi.htm----->
def search_mtoto(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(fname__contains=query_original)|Q(tname__contains=query_original)|Q(reg_no__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = RegisteredPatients.objects.filter(search)
    mylist= []
    mylist += [x.fname + '   ' + x.tname for x in queryseti]

    return JsonResponse(mylist, safe=False)

def search_MyUsers_autocomplete(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(username__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = MyUser.objects.filter(search)
    mylist= []
    mylist += [x.username for x in queryseti]

    return JsonResponse(mylist, safe=False)

def search_clinic_service(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(ServiceName__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryseti = ClinicServices.objects.filter(search)
    mylist= []
    mylist += [x.ServiceName  for x in queryseti]

    return JsonResponse(mylist, safe=False)


#VIEWS KWA AJILI YA DOZI ZINZISHIA HAPA








#HIZI ZA CHININI VIEWS KWAAJILI YA VIPIMO KWA WATOTO TU ZINAANZIA HAPA
#KWA  AJILL YA KUADD VIPIMO VYA WATOTO
def add_kipimo(request):
    
    form = VipimoForm(request.POST or None)
    total_dozi = Vipimo.objects.count()
    kipimo = Vipimo.objects.order_by('-id')[:3]  #hii ni kwa recent dozi
    if form.is_valid():
        form.save()
        return redirect('list_kipimo')
    context = {
        "form":form,
        "title":"New Dozi",
        "total_dozi":total_dozi,
        "kipimo":kipimo
    }
    return render(request, 'hospital/add_kipimo.html', context)

#KWA AJILI YA KUDISPLAY VIPIMO VYA WATOTO KWENYE LIST VIPIMO.HTML
def list_kipimo(request):
    title = 'List of Vipimo'
    kipimo = Vipimo.objects.filter(paid=False).order_by('-id')
    form = DoziSearchForm(request.POST or None)# form ya kuserch ila nimeifuta nimetumia hzo code za chini

    context = {
        "title":title,
        "kipimo":kipimo,
        "form":form
    }
    #searching button codes
    if request.method == 'POST':
        kipimo = Vipimo.objects.filter( name__icontains=form['name'].value())

    context = {
        "form":form,
        "title":title,
        "kipimo":kipimo
    }

    return render(request, 'hospital/list_vipimo.html', context)

#KWA AJILI YA KUAPDATE KIPIMO CHA MTOTO KWENYE LIST KIPIMO.HTML
def kipimo_update(request, pk):
    queryset = Vipimo.objects.order_by('-id')[:2]

    querySet = Vipimo.objects.get(id=pk)
    form = VipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = VipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            return redirect('/list_kipimo')
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/add_kipimo.html', context)

#KWA AJILI YA KUDELETE KIPIMO CHA MTOTO KWENYE LIST KIPIMO.HTML
def kipimo_delete(request, pk):
    watoto = get_object_or_404(Vipimo, id=pk)
    watoto.delete()
    return redirect('list_kipimo')

#HII NI YA KUACCEPT VIPIMO KWA AJILI YA WATOTO KWENYE SINGLE KIPIMO LIST.HTML
def accept_vipimo(request, id):
    queryset = Vipimo.objects.order_by('-id')[:2]

    querySet = Vipimo.objects.get(id=id)
    form = VipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = VipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ADDED SUCCESSFULLY")
            return redirect('accept_vipimo',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_kipimo_list.html', context)
#HIIYA ADD DAWA HAITUMIKI KWA SASA ILIKUWA NI YA WATOTO KWENYE SINGLE LIST DETAIL.HTML
def add_dawa(request, id):
    queryset = Vipimo.objects.order_by('-id')[:2]

    querySet = Vipimo.objects.get(id=id)
    form = VipimoUpdateForm(instance=querySet)
    if request.method == "POST":
        form = VipimoUpdateForm(request.POST, instance=querySet)
        if form.is_valid():
            form.save()
            messages.success(request, "ALL MEDICINES ARE ACCEPTED SUCCESSFULLY")
            return redirect('add_dawa',id)
        messages.add_message(request, messages.SUCCESS, " invalid")

        return HttpResponseRedirect(request.path)

            


            
            #messages.add_message(request, messages.SUCCESS, " has accepted")

            #return HttpResponseRedirect(request.path)  
            
    
    context = {
        "form":form,
        "querySet":querySet,
        "queryset":queryset
        
    }
    return render(request, 'hospital/single_kipimo_list.html', context)

#YA KUSERACH KIPIMO KWA WATOTO KWENYE LIST_VIPIMO.HTML
def search_kipimo2(request):
    print(request.GET)
    query_original = request.GET.get('term')
    search = Q(name__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    queryset = Vipimo.objects.filter(search)
    mylist= []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)


#VIEWS KWA AJILI YA VIPIMO ZINAISHIA HAPA






