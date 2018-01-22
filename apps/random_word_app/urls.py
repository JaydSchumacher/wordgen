from django.conf.urls import url
from . import views


def test(request):
    print "we are in reset"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate$', views.generate),
    url(r'^reset', views.reset),
]