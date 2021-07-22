from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):
    length= int(request.GET.get('length',10))
    the_password=''
    characters = list('abcdefghjimnokstuwvqlxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHLMNOPQSTURKIJYVWXZ'))
    if request.GET.get('special'):
        characters.extend(list('@#$%^&*()!'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        the_password+=random.choice(characters)


    return render(request, 'generator/password.html',{'password': the_password})
def about(request):
    return render(request,'generator/about.html')