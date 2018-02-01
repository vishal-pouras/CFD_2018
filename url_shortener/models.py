from django.db import models
from django.urls import reverse


class Link(models.Model):
    long_url = models.URLField()
    your_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('url_shortener:link_create')

    def __str__(self):
        return self.long_url + ' - ' + self.your_name
