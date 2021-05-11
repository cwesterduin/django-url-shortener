from django.shortcuts import render
from .models import Url

# Create your views here.
def myFunc(a):
    return {
        "url": a['url'],
        "mongo_id": a['_id']
        }

def urls(req):
    urls = {'urls': list(Url.objects.all().values('url', '_id'))}
    newUrls = map(myFunc, urls['urls'])
    print(newUrls)
    return render(req, 'url.html', {'urls':newUrls}) 