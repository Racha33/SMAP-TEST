from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.HomepageView, name='homepage'),
    url(r'^summary/', views.summary, name='summary'),
    url(r'^detail/', views.detail, name='detail')
]
