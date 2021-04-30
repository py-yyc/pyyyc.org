from django import template

register = template.Library()


@register.filter(name="format")
def format_(value, arg):
    return format(value, arg)
