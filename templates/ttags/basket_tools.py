from django import template
# from django.conf import settings

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


# @register.filter(name='calc_free_delivery_bottles')
# def calc_free_delivery_bottles(quantity, settings.FREE_DELIVERY_THRESHOLD):
