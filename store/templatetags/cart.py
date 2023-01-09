from django import template
register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys=cart.keys()
    product=product.id
    for id in keys:
        if int(id)==product:
            return True
    return False

@register.filter(name='product_quantity')
def product_quantity(product, cart):
    keys=cart.keys()
    product=product.id
    for id in keys:
        if int(id)==product:
            return cart.get(id)
    return False

@register.filter(name='total_price')
def total_price(product, cart):
    return product.price * product_quantity(product, cart)

@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum=0
    for p in products:
        sum +=  total_price(p, cart)
    return sum