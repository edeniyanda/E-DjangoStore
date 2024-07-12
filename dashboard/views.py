from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item


@login_required
def index(request):
    items_by_user = Item.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {
        "items" : items_by_user
    })
