from urlshorter import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^mainpage', views.mainpage, name = 'mainpage'),
]