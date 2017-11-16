from django.shortcuts import render, redirect
from .forms import UrlsForm
from .urlshort import add_shorted_url
from .models import Url

def mainpage(request):
    form = UrlsForm()
    if request.method == "POST":
        url = request.POST.get("URL")
        #add record to db and received Code
        received_code = add_shorted_url(url)#returned short_url
        form = UrlsForm({'Code':received_code, 'URL':url})
        ##new_form = form.save()
    return render(request, 'urlshorter/mainpage.html', locals())

def trans_to_shorturl(self):
    #getting long_url by filtered "Code"
    long_url = Url.objects.get(Code='http://127.0.0.1:8000/3');
    print(long_url.Code)
    return redirect(long_url.URL)



