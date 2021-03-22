from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html', {'greeting' : 'Hello!'})

def reverse(request):
    #user_text_list = []
    user_text = request.GET['usertext']
    reverse_text = user_text[::-1]
    #user_text_list = user_text

    split_list = user_text.split()

    count = 0
    for items in split_list:
        count +=1
    count_items = count

    return render(request, 'reverse.html', {'usertext' : user_text, 
    'reverstext' : reverse_text, 'countitems' : count_items},)


