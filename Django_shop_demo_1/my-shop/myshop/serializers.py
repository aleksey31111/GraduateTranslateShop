
from shop import CartModel
from shop import AddToCartSerializer


class AddSmartPhoneToCartSerializer(AddToCartSerializer):
    """
    Modified AddToCartSerializer which handles SmartPhones
    """

    def get_instance(self, context, data, extra_args):
        product = context['product']
        request = context['request']
        try:
            cart = CartModel.objects.get_from_request(request)
        except CartModel.DoesNotExist:
            cart = None
        try:
            variant = product.get_product_variant(
                product_code=data['product_code'])
        except (TypeError, KeyError, product.DoesNotExist):
            variant = product.variants.first()
        instance = {
            'product': product.id,
            'product_code': variant.product_code,
            'unit_price': variant.unit_price,
            'is_in_cart': bool(product.is_in_cart(cart, product_code=variant.product_code)),
            'extra': {'storage': variant.storage},
            'availability': variant.get_availability(request),
        }
        return instance
