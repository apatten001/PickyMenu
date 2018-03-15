from django import forms

from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(max_length=120, required=False)
    category = forms.CharField(max_length=120, required=False)


class RestaurantCreateForm2(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [ 'name',
                   'location',
                   'category',
                   'slug',

        ]

