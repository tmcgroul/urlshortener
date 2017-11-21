from django.shortcuts import render, redirect, get_object_or_404
from .forms import UrlsForm
from .urlshort import add_shorted_url
from .models import Url

def mainpage(request):
    form = UrlsForm()
    if request.method == "POST":
        url = request.POST.get("URL")
        #add record to db and received Code
        received_code = add_shorted_url(url)#returned short_url
        if received_code != None:
            form = UrlsForm({'Code':received_code, 'URL':url})
    return render(request, 'urlshorter/mainpage.html', locals())

def trans_to_shorturl(self, shortcode=None):
    #getting long_url by filtered "Code"
    shortcode = 'http://127.0.0.1:8000/' + shortcode
    long_url = get_object_or_404(Url, Code=shortcode)
    return redirect(long_url.URL)



