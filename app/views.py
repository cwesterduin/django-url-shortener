from django.shortcuts import render, redirect
from .models import Url
from djongo import models
from bson.objectid import ObjectId

# Create your views here.
def parseObjIds(a):
    return {
        "url": a['url'],
        "mongo_id": a['_id']
        }

def urls(req):
    urls = list(Url.objects.all().values('url', '_id'))
    print(urls)
    newUrls = {'urls' : map(parseObjIds, urls)}
    return render(req, 'url.html', newUrls) 

# def show(req, id):
#     print('*************************')
#     print(id)
#     obj = Url.objects.get(_id=ObjectId(id))
#     newObj = {
#         "url": obj.url,
#         "mongo_id": obj._id
#     }
#     return render(req, 'test.html', {"url": newObj}) 

def redirector(req, id):
    obj = Url.objects.get(_id=ObjectId(id))
    response = redirect(obj.url)
    return response