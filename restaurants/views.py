# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,HttpResponse, get_object_or_404,HttpResponseRedirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import RestaurantLocation
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from .utils import unique_slug_generator
from .forms import RestaurantCreateForm2
# Create your views here.


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantCreateForm2
    template_name = 'restaurants/form.html'
    # success_url = '/restaurants/'
    login_url = '/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args,**kwargs):
        context = super(RestaurantCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantCreateForm2
    template_name = 'restaurants/form-update.html'
    # success_url = '/restaurants/'
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Update Restaurant'
        return context

    def get_queryset(self):
        queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        queryset = RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset

    # def get_queryset(self):
    #     return RestaurantLocation.objects.all(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        queryset = RestaurantLocation.objects.filter(owner=self.request.user)
        return queryset





    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    # def get_object(self,*args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, pk=rest_id)
    #     return obj


def rl_pre_save_reciever(sender, instance, *args,**kwargs):
    print('saving...')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug  = unique_slug_generator(instance)

# def rl_post_save_reciever(sender, instance, created, *args,**kwargs):
#     print('saved')
#     print(instance.timestamp)


pre_save.connect(rl_pre_save_reciever, sender=RestaurantLocation)

# post_save.connect(rl_post_save_reciever, sender=RestaurantLocation)







