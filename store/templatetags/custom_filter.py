from django import template
register=template.Library()

@register.filter(name="currency")
def currency(number):
    return "₹ " + str(number)

@register.filter(name="order_price")
def order_price(number, quantity):
    return number*quantity
