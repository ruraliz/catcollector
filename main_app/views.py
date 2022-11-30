from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#temp add Cats class

class Cat:
    def __init__(self,name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
    def __str__(self):
        return f"{self.name}"

cats = [
    Cat('Rufus', 'tabbycat', 'crazy cat', 103),
    Cat('Simba', 'lion', 'brava', 5),
    Cat('Garfield', 'tabbycat', 'likes lasagna', 43)
]
def index(request):
    return render(request, 'index.html', {cats: cats})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')