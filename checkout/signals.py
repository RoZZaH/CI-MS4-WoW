from django.core.signals import request_finished
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem, Order

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()


# @receiver(post_save, sender=Order)
# @receiver(request_finished)
# def del_session_basket(sender, **kwargs):
#     """
#     remove session basket
#     """
#     print("baseket removed")
    # if "basket" in self.request.session:
    #     del self.request.session['basket']

# post_save.connect(del_session_basket, sender=Order)