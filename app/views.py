from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def dsform(request):
    form=emplyoee()
    d={'form':form}
    if request.method=='POST':
        data=emplyoee(request.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            age=data.cleaned_data['age']
            number=data.cleaned_data['number']
            email=data.cleaned_data['email']
            addr=data.cleaned_data['address']
            gen=data.cleaned_data['gender']
            lan=data.cleaned_data['language']
            d1={'name':name,'age':age,'number':number,'email':email,'address':addr,'gender':gen,'language':lan}
            return render(request, 'display.html',d1)
        
    return render(request, 'dsform.html',d)
