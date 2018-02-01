from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Link


class LinkCreate(CreateView):
    model = Link
    fields = ['long_url', 'your_name', 'description']


class IndexView(generic.ListView):
    template_name = 'url_shortener/list.html'
    context_object_name = 'all_links'

    def get_queryset(self):
        return Link.objects.all()

