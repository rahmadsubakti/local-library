from django import template

from catalog.models import Genre

register = template.Library()

@register.inclusion_tag('catalog/genre_list.html')
def genres():
    return {'genres': Genre.objects.all()}