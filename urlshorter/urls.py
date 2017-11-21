from urlshorter import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^mainpage', views.mainpage),
    url(r'^(?P<shortcode>[\w-]+)/$', views.trans_to_shorturl),
]