from django.urls import path

from .views import ItemListView,ItemDetailView,ItemCreateView,ItemUpdateView

app_name = 'menu'

urlpatterns = [
    path('', ItemListView.as_view(), name='list'),
    path('<int:pk>/', ItemUpdateView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name='create'),

]