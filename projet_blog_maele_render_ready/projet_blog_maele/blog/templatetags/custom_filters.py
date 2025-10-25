from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Divise une chaîne selon le séparateur donné
    Usage: {{ value|split:"," }}
    """
    return value.split(arg)

@register.filter
def trim(value):
    """
    Retire les espaces au début et à la fin d'une chaîne
    Usage: {{ value|trim }}
    """
    return value.strip() if value else value