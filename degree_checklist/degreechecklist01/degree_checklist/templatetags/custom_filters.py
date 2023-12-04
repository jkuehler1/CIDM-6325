from django import template

register = template.Library()

@register.filter(name='uppercase')
def uppercase(value):
    """Converts a string into all uppercase."""
    return value.upper()
