from django.shortcuts import render, get_object_or_404,Http404, redirect
from django.views.generic import DetailView, View,CreateView,ListView
from django.contrib.auth import get_user_model
from restaurants.models import RestaurantLocation
from menus.models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import RegisterForm

# Create your views here.

User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/login'

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/logout')
        return super(RegisterView, self).dispatch(*args, **kwargs)


class ProfileFollowToggle(LoginRequiredMixin, View):
    def post(self,request, *args, **kwargs):
        username_to_toggle = request.POST.get('username')
        profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
        return redirect(f'/profile/{profile_.user.username}/')


class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        print(context)
        user = context['user']
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        query = self.request.GET.get('q')
        items_exist = Item.objects.filter(user=user).exists()
        qs = RestaurantLocation.objects.filter(owner=self.get_object()).search(query)

        if items_exist and qs.exists():
            context['location'] = qs
        return context


class ProfileListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Profile.objects.all()




