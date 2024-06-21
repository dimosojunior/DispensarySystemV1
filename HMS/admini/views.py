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


# Create your views here.
def index(response):
    
    
    return render(response, 'admini/index.html')








#MWISHO WA YOTE NI HAPO


def all_time_payment(request):
    
    payment = KawaidaDozi.objects.filter(paid=True).order_by('-id')
    

    context = {
        
        "payment":payment
    }

    return render(request, 'admini/all_time_payment.html', context)


def today_payment(request):

	start_date = datetime.date(2021,10,13)
	end_date = datetime.date(2021,12,30)

	myDate = datetime.datetime.now()
	myDate1 = datetime.datetime.now().date()
	myDate2 = datetime.datetime.now().time()

	payment = KawaidaDozi.objects.filter(paid=True).order_by('-id')

    
    

	context = {
	    
	    "payment":payment,
	    "myDate":myDate,
	    "myDate1":myDate1,
	    "myDate2":myDate2
	}

	return render(request, 'admini/today_payment.html', context)


class add_available_medicines(SuccessMessageMixin, CreateView):
    model = ClinicServices
    template_name = 'admini/add_available_medicines.html'
    form_class = ClinicServicesForm
    success_url = reverse_lazy('add_available_medicines')
    success_message = "Service was added Successfully"


class update_available_medicines(SuccessMessageMixin, UpdateView):
    model = ClinicServices
    template_name = 'admini/add_available_medicines.html'
    form_class = ClinicServicesForm
    success_url = reverse_lazy('Clinic_services_Categories_Page')
    success_message = "Service was Updated Successfully"

def delete_available_medicines(request, pk):
    medicine = get_object_or_404(ClinicServices, id=pk)
    messages.info(request, "Service was deleted Successfully")
    medicine.delete()
    return redirect('Clinic_services_Categories_Page')

def search_available_medicines(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ServiceName__contains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    available_medicines = ClinicServices.objects.filter(search)
    mylist= []
    mylist += [x.ServiceName for x in available_medicines]
    return JsonResponse(mylist, safe=False)

