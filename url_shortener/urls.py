from django.conf.urls import url
from . import views


app_name = 'url_shortener'

urlpatterns = [
    url(r'^add/$', views.LinkCreate.as_view(), name='link_create')
]