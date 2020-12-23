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


@receiver(post_save, sender=Order)
def associate_order(sender, instance, **kwargs):
    """
    assocaite Order with logged in user and remove session basket
    """
    if instance.customer:
        print(instance.customer)

    #     profile = Customer.objects.get(user=request.user)
    #     order.user_profile = profile
    #     order.save()

    #     if save_info:
    #          profile_data = {
    #             'default_phone_number': order.phone_number,
    #             'default_country': order.country,
    #             'default_postcode': order.postcode,
    #             'default_town_or_city': order.town_or_city,
    #             'default_street_address1': order.street_address1,
    #             'default_street_address2': order.street_address2,
    #             'default_county': order.county,
    #         }
    #         user_profile_form = UserProfileForm(profile_data, instance=profile)
    #         if user_profile_form.is_valid():
    #             user_profile_form.save()


    # print("baseket removed")
    # if "basket" in self.request.session:
    #     del self.request.session['basket']

# post_save.connect(del_session_basket, sender=Order)