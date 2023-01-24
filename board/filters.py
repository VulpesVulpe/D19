import django_filters
from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Category



class PostFilter(FilterSet):
    date__gt = DateFilter(widget=DateInput(attrs={'type': 'date'}), field_name='date', lookup_expr='gt')
    category__name = ModelChoiceFilter(field_name='category', queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = {'title': ['icontains']}

