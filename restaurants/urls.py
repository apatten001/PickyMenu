from .views import *
from django.urls import path

app_name = 'restaurants'
urlpatterns = [
    path('<slug>/', RestaurantUpdateView.as_view(), name='detail'),
    path('create', RestaurantCreateView.as_view(), name='create'),
    # path('<slug>/edit/', RestaurantUpdateView.as_view(), name='edit'),
    path('', RestaurantListView.as_view(), name='list'),

]