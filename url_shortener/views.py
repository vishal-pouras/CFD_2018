from django.views.generic.edit import CreateView, UpdateView
from .models import Link


class LinkCreate(CreateView):
    model = Link
    fields = ['long_url', 'your_name', 'description']
