from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import newtours


# Create your views here.
def homepage(req):
    return render(req,'navigation.html')

def tours(req):
    page = loader.get_template('tours.html')
    response = page.render({},req)
    return HttpResponse(response)

def bookmytrip(req):
    page = loader.get_template('bookmytrip.html')
    place = newtours.objects.all()
    data = {'places':place}
    response = page.render(data,req)
    return HttpResponse(response)

def tourdetails(req):
    page = loader.get_template('tourdetails.html')
    place = newtours.objects.all()
    data = {'details':place}
    response = page.render(data,req)
    return HttpResponse(response)

def about_us(req):
    page = loader.get_template('about_us.html')
    response = page.render({},req)
    return HttpResponse(response)

def rating(req):
    page = loader.get_template('rating.html')
    response = page.render({},req)
    return HttpResponse(response)