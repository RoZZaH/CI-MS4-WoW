from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Customer(models.Model):
    """
    A Customer profile model for delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    primary_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    primary_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    primary_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    primary_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    primary_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    primary_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the customer profile
    """
    if created:
        Customer.objects.create(user=instance)
    # Existing users: just save the profile
    instance.customer.save()