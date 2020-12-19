from django.conf import settings
from decimal import Decimal
from django.db.models.functions import Coalesce
from wines.models import Wine 
from django.shortcuts import get_object_or_404


def basket_contents(request):

    basket_items = []
    total = 0
    bottle_count = 0
    delivery_charge = 0
    basket = request.session.get("basket", {})

    for bottle_id, quantity in basket.items():
        bottle = get_object_or_404(Wine, slug=bottle_id)
        _price =  (bottle.discounted_price if bottle.discounted_price \
                    is not None else bottle.list_price)
        total += quantity * _price
        bottle_count += quantity
        basket_items.append({
            "bottle_id": bottle.slug,
            "quantity": quantity,
            "bottle": bottle
        })

    if bottle_count < settings.FREE_DELIVERY_THRESHOLD:
        if bottle_count <= 2:
            delivery_charge = Decimal(settings.STANDARD_DELIVERY_CHARGE)
        if bottle_count <= 5:
            delivery_charge = Decimal(2 * settings.STANDARD_DELIVERY_CHARGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bottle_count
    else:
        delivery_charge = 0
        free_delivery_delta = 0
    

    context =  {
        "basket_items": basket_items,
        "total": total,
        "bottle_count": bottle_count,
        "delivery_charge": delivery_charge,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": total,
    }

    return context