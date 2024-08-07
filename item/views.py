from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, Category
from .forms import NewItemForm, EditItemForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
    return render(request, "item/detail.html", {
        "item": item,
        "related_items": related_items,
    })

def itemsall(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category = category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, "item/itemsall.html", {
        "items" : items, 
        "query" : query,
        "categories": categories,
        "category_id" : category_id
    })

@login_required
def newitem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/form.html", {
        "form" : form,
        "title" : "New Item",
    })

@login_required
def edititem(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        print("Post rewuest made ")
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = EditItemForm(instance=item)
        print("Heelo")
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})


@login_required
def delete_item(request, pk):
    item_to_delete = get_object_or_404(Item,pk=pk)
    item_to_delete.delete()
    return redirect("dashboard:dashboard_page")
