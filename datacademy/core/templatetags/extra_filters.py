from django import template
import re

register = template.Library()


@register.filter
def slugify_under(string):
    string = re.sub('\s+', '_', string)
    string = re.sub('[^\w.-]', '', string)
    string = re.sub('-','', string)
    string = re.sub('\.','', string)
    return string.strip('_.- ').lower()
