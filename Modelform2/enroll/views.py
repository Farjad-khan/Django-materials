from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            #print(nm)
            #print(em)
            #print(pwd)
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/userRegistration.html', {'form':fm})