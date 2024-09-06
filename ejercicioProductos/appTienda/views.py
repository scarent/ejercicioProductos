from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'appTemplates/index.html') #app/archivo

def electronica(request):
    data = {"Nombre" : "Electronica",}
    
    