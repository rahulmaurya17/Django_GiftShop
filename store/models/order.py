from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.IntegerField(default=1)
    date=models.DateField(default=datetime.datetime.today)
    address=models.CharField(max_length=50, default='', blank=True)
    phone=models.CharField(max_length=50, default='', blank=True)
    status=models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customerID):
        return Order.objects.filter(customer=customerID).order_by("-date")