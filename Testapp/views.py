from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return render(request,'index.html')


def Hobbie_page(request):
    return render(request,'Hobbie.html')


def Pet_page(request):
    return render(request,'Pet.html')

def Font_page(request):
    return render(request,'Font.html')