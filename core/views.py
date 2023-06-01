import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.template.context_processors import csrf

from core.models import *


def default_context(request, alias, obj):
    data = get_object_or_404(obj, alias=alias)
    csrf_token = csrf(request)

    last_modified = data.last_modified.strftime('%a, %d %b %Y %H:%M:%S GMT')
    context = {
        'data': data,
        'csrf_token': csrf_token,
        'last_modified': last_modified,
        # 'seo_info': seo_info
    }

    return context


def index(request):
    context = default_context(request, "index", TextPage)
    template = loader.get_template('index.html')

    gallery = Gallery.objects.all()
    news = News.objects.all()[:2]
    reviews = Review.objects.all()

    context.update({
        'gallery': gallery,
        'news': news,
        'reviews': reviews
    })

    return HttpResponse(template.render(context))


def about(request):
    context = default_context(request, "about", TextPage)
    template = loader.get_template('about.html')

    return HttpResponse(template.render(context))


def news(request):
    context = default_context(request, "news", TextPage)
    template = loader.get_template('news.html')
    news = News.objects.all()

    context.update({
        'news': news
    })

    return HttpResponse(template.render(context))


def news_item(request, alias):
    context = default_context(request, alias, News)
    template = loader.get_template('news-item.html')

    return HttpResponse(template.render(context))


def contacts(request):
    context = default_context(request, "contacts", TextPage)
    template = loader.get_template('contacts.html')

    return HttpResponse(template.render(context))


def reviews(request):
    context = default_context(request, "reviews", TextPage)
    template = loader.get_template('reviews.html')

    reviews = Review.objects.all()

    context.update({
        'reviews': reviews
    })

    return HttpResponse(template.render(context))


def ajax(request):
    result = False
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('type') == 'callback':
            result = create_order(['name', 'phone', 'comment'], data)
        if data.get('type') == 'reviews':
            result = create_review(['name', 'text'], data)
    return JsonResponse({'created': result})


def create_order(names: list, data: dict, ):
    obj_info = {}
    message = f''
    for name in names:
        obj_info[name] = data.get(name, '')
        message += f'{Order._meta.get_field(name).verbose_name}: {data.get(name, "")}\n'
    requests.get(
        f'https://api.telegram.org/bot6286171380:AAF1gCE9uUTzi9SSTYmHKl7P0xphvcSgrrY/sendMessage?chat_id=-812752353&text={message}')
    Order.objects.create(**obj_info)
    return True


def create_review(names: list, data: dict):
    obj_info = {}
    for name in names:
        obj_info[name] = data.get(name, '')
    Review.objects.create(**obj_info)
    return True
