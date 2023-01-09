from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.order import Order


class CheckOut(View):
    def post(self, request):
        # print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),
                          address=address,
                          phone=phone)
            order.placeOrder()

        request.session['cart'] = {}
        return redirect('cart')
