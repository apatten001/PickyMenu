from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Q

# Create your models here.
User = settings.AUTH_USER_MODEL


class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self, query):
        if query:
            return self.filter(
                Q(name__icontains=query) |
                Q(location__icontains=query) |
                Q(category__icontains=query) |
                Q(item__name__icontains=query) |
                Q(item__contents__icontains=query)).distinct()
        else:
            return self


class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self.db)

    def search(self, query):
        return self.get_queryset().search(query)


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=60 ,null=True, blank=True)
    timestamp = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    objects = RestaurantLocationManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name




