from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.order import Order


class Orders(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)

        return render(request, "order.html", {"orders": orders})
