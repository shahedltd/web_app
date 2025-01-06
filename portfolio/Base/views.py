from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base import models
from Base.models import Contact
# Create your views here.


# def home(request):
#    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        print('post')

        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        number = request.POST.get('number')

        print(name, email, content, number)

        if len(name) > 3 and len(name) < 30:
            pass
        else:
            messages.error(request, 'Length of name should be greater than 3 and less than 30 words.')
            return render(request, 'home.html')
        
        if len(email) > 1 and len(email) < 40:
            pass
        else:
            messages.error(request, 'Invalid Email, try again.')
            return render(request, 'home.html')
        
        if len(number) > 8 and len(number) < 13:
            pass
        else:
            messages.error(request, 'Invalid Phone Number.')
            return render(request, 'home.html')
        
        ins = models.Contact(name=name, email=email, content=content, number=number)
        ins.save()

        messages.success(request, 'Your message has been sent successfully. Thank you so much for your feedback!')
        print('The data has been written to the database.')
        print('The request is no pass.')
    
    return render(request, 'home.html')
        