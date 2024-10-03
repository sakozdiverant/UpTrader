from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import MenuItem

def homepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def menu_view(request):
    menu_items = MenuItem.objects.filter(parent=None)  # Получаем корневые элементы меню
    return render(request, 'menu/draw_menu.html', {'menu_items': menu_items})

def sub_menu(request):
    menu_items = MenuItem.objects.filter(parent=None)  # Получаем корневые элементы меню
    return render(request, 'menu/sub_menu.html', {'menu_items': menu_items})