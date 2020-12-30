from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def is_homepage(context):
    if context.request.path == "/":
        return "homepage"
    else:
        return "not_homepage"