from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html', {'greeting' : 'Hello!'})

def reverse(request):
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext' : user_text, 
    'reverstext' : reverse_text},)
