from django.shortcuts import render
from .forms import UrlsForm

def mainpage(request):
    form = UrlsForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        new_form = form.save()

    return render(request, 'urlshorter/mainpage.html', locals())
