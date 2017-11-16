from urlshorter import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^mainpage', views.mainpage),
    #url(r'^[0-9]', views.trans_to_shorturl),
    url(r'^(?P<shortcode>[\w-]+)/$', views.trans_to_shorturl),
    #url(r'^[0-5]', views.trans_to_shorturl),
]