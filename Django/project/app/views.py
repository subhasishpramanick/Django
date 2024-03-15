from django.shortcuts import render
from django.http import HttpResponse
from .models import contactdetails

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        Name=request.POST['name']
        Email=request.POST['email']
        Query=request.POST['ques']
        new = contactdetails(name=Name,email=Email,query=Query)
        new.save()
        
        user_contact_details=contactdetails.objects.all()
        context={
            'C_details':user_contact_details
        }
        
    return render(request,'contact.html',context)
    