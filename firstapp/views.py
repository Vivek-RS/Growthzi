
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        response = f'Welcome, {name}. Your registered email is {email}'
        return HttpResponse(response)
    else:
        return HttpResponse('Invalid request method')

