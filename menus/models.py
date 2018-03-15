from django.conf import settings
from django.db import models
from restaurants.models import RestaurantLocation
from django.urls import reverse


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.CASCADE)
    #item stuff
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separate each item by a comma.')
    excludes = models.TextField(blank=True, null=True, help_text='Separate each item by a comma.')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-updated', '-timestamp']  # orders time from most recent with the - sign

    def get_absolute_url(self):
        return reverse('menu:detail', kwargs={'pk': self.pk})

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes(self):
        return self.excludes.split(',')

    def __str__(self):
        return self.name





