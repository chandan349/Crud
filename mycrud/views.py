from django.shortcuts import render
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')


def add_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        item = Item(name=name, description=description)
        item.save()
        messages.info(request, 'Item added successfully')
    else:
        pass

    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }

    return render(request, 'index.html')