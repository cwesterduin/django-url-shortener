from django.shortcuts import render
from .models import Url

# Create your views here.
def parseObjIds(a):
    return {
        "url": a['url'],
        "mongo_id": a['_id']
        }

def urls(req):
    urls = list(Url.objects.all().values('url', '_id'))
    newUrls = {'urls' : map(parseObjIds, urls)}
    return render(req, 'url.html', newUrls) 