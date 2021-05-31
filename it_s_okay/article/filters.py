from django.contrib.auth.models import User,Group
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from .models import Article
from django import forms

class UserFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    category = ModelMultipleChoiceFilter(
        queryset = Group.objects.all(),
        widget = forms.CheckboxSelectMultiple

    )

    class Meta:
        model = Article
        fields =[
            'title',
            'category',
            'age',
    ]
