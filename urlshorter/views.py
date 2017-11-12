from django.shortcuts import render
from .forms import UrlsForm
from .urlshort import add_shorted_url

def mainpage(request):
    form = UrlsForm(request.POST or None)
    if request.method == "POST":
        url = request.POST.get("URL")
        add_shorted_url(url)

        ##new_form = form.save()

    return render(request, 'urlshorter/mainpage.html', locals())
