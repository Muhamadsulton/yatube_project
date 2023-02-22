from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return  HttpResponse('Список постов группы')

def group_posts_details(request, any_slug):
    return  HttpResponse(f'Пост номер {any_slug}')