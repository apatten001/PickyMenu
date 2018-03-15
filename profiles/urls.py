from .views import ProfileDetailView, ProfileListView
from django.urls import path

app_name = 'profiles'

urlpatterns= [
    path('list/', ProfileListView.as_view(), name='profile_list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),


]

