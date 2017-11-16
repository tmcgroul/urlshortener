from urlshorter import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^mainpage', views.mainpage, name = 'mainpage'),
    url(r'^djopa6', views.trans_to_shorturl, name='redirect'),
]