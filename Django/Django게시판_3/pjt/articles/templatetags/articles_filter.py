from atexit import register
from django import template

register = template.Library()

@register.filter
def sub(value,arg):
    return value - arg