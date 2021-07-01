from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blogpost',
        'content': 'First post',
        'date_posted': '24.07.2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blogpost 2',
        'content': 'Second post',
        'date_posted': '30.09.2001'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'mainview/home.html', context)        #Zeigt auf das Template home.html


def about(request):
    return render(request, 'mainview/about.html', {'title': 'About'})  # Zeigt auf das Template about.html