from django.shortcuts import render, redirect
from .models import Url
from djongo import models
from bson.objectid import ObjectId
from .forms import NewUrlForm
from django.contrib import messages

# Create your views here.
def parseObjIds(a):
    return {
        "url": a['url'],
        "mongo_id": a['_id']
        }

def urls(req):
    if req.method == 'POST':
        url = NewUrlForm(req.POST)
        newUrl = url.save()
        response = redirect("urls-show", id=newUrl._id)
        return response
    else:
        urls = list(Url.objects.all().values('url', '_id'))
        form = NewUrlForm()
        data = {'urls' : map(parseObjIds, urls), 'form': form}
        return render(req, 'url.html', data) 

def show(req, id):
    try:
        obj = Url.objects.get(_id=ObjectId(id))
        data = {
            "url": obj.url,
            "mongo_id": obj._id
        }
        return render(req, 'test.html', {"url": data}) 
    except:
        return redirect("urls-all")


def redirector(req, id):
    try:
        obj = Url.objects.get(_id=ObjectId(id))
        response = redirect(obj.url)
        return response
    except:
        # urls = list(Url.objects.all().values('url', '_id'))
        # form = NewUrlForm()
        # trying to pass an error message with a redirect
        # data = {'urls' : map(parseObjIds, urls), 'form': form, 'err' : 'no shortended url found for that id, create one?'}
        # return render(req, 'url.html', data) 
        return redirect("urls-all")

def not_found_404(req, exception):
    urls = list(Url.objects.all().values('url', '_id'))
    data = {'urls' : map(parseObjIds, urls)}
    return render(req, 'url.html', data) 
