from django.shortcuts import render
from .forms import UrlsForm
from .urlshort import add_shorted_url

def mainpage(request):
    form = UrlsForm()
    if request.method == "POST":
        url = request.POST.get("URL")
        #add record to db and received Code
        received_code = add_shorted_url(url)
        form = UrlsForm({'Code':received_code, 'URL':url})
        ##new_form = form.save()

    return render(request, 'urlshorter/mainpage.html', locals())
