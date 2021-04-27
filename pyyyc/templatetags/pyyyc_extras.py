from django import template

register = template.Library()


@register.filter
def strftime(value, arg):
    return value.strftime(arg)
