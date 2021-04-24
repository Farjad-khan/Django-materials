from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            #normal way
            messages.add_message(request, messages.SUCCESS, 'Your Account has been created!')
            # shortcut way
            messages.info(request, 'Now You can Log In')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/UserRegistration.html', {'form': fm})
