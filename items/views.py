from django.shortcuts import render
from .models import Item
# Create your views here.

# def item(request):
#     return render(request, 'index.html')

def item_list(request):
    items = Item.objects.all().order_by('-created_at') # yangi qo'shilgan ma'lumotlar tepada chiqadi
    return render(request, 'index.html' , {'items':items})
