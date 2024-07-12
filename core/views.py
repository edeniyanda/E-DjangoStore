from django.shortcuts import render
from item.models import (Category, Item)
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()

    context = {
        "categories" : categories,
        "items" : items,
    }
    return render(request, "core/index.html", context=context)

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    form = SignUpForm()

    return render(request, "core/signup.html", {
        "form" : form   
    })