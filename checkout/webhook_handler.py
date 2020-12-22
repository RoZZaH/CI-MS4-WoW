from django.http import HttpResponse
from .models import Order, OrderLineItem
from wines.models import Wine

import json, time

class StripeWebHook_Handler:
    """Handle STRIPE webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled webhook receievd: {event["type"]}',
            status=200
        )
   
    def handle_payment_intent_succeeded(self, event):
        """
        handle payment succedeed webhook event
        """
        intent = event.data.object
        # print(intent)
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field,value in shipping_details.address.items():
            if value == "" :
                shipping_details.address[field] = None
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                            full_name__iexact=shipping_details.name,
                            email__iexact=billing_details.email,
                            phone_number__iexact=shipping_details.phone,
                            country__iexact=shipping_details.address.country,
                            postcode__iexact=shipping_details.address.postal_code,
                            town_or_city__iexact=shipping_details.address.city,
                            street_address1__iexact=shipping_details.address.line1,
                            street_address2__iexact=shipping_details.address.line2,
                            county__iexact=shipping_details.address.state,
                            grand_total=grand_total,
                            original_basket=basket,
                            stripe_pid=pid,
                        )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook receievd: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                            full_name=shipping_details.name,
                            email=billing_details.email,
                            phone_number=shipping_details.phone,
                            country=shipping_details.address.country,
                            postcode=shipping_details.address.postal_code,
                            town_or_city=shipping_details.address.city,
                            street_address1=shipping_details.address.line1,
                            street_address2=shipping_details.address.line2,
                            county=shipping_details.address.state,
                            original_basket=basket,
                            stripe_pid=pid)

                for bottle_id, quantity in json.loads(basket).items():
                    product = Wine.objects.get(slug=bottle_id)
                    _price =  (product.discounted_price if product.discounted_price \
                                is not None else product.list_price)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save(price=_price)
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook receievd: {event["type"]} | ERROR: {e}',
                    status=500
                )
        return HttpResponse(
            content=f'Webhook receievd: {event["type"]} | SUCCESS: created Order with webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        handle a payment failed webhook event
        """

        return HttpResponse(
            content=f'Webhook receievd: {event["type"]}',
            status=200
        )