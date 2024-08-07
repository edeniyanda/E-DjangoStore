from django.shortcuts import render, redirect
from item.models import (Category, Item)
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()

    context = {
        "categories" : categories,
        "items" : items,
    }
    return render(request, "core/index.html", context=context)

def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect("/login")
    else:
        form = SignUpForm()

    return render(request, "core/signup.html", {
        "form" : form   
    })