from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='calc_lineitem_each')
def calc_lineitem_each(total, quantity):
    return total / quantity
