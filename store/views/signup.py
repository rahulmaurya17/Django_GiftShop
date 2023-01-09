from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        # validations:
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        # saving
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("login")
        else:
            data = {
                'error': error_message,
                'value': values
            }
            return render(request, "signup.html", data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name is required!!!!"
        elif len(customer.first_name) < 4:
            error_message = "First Name length must be 4 charater or more."
        elif not customer.last_name:
            error_message = "Last Name is required!!!!"
        elif len(customer.last_name) < 4:
            error_message = "Last Name length must be 4 charater or more."
        elif not customer.phone:
            error_message = "Phone Number is required!!!!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 charater"
        elif len(customer.phone) > 10:
            error_message = "Phone Number must be 10 charater"
        elif len(customer.email) < 5:
            error_message = "Email must br 5 character or more"
        elif not customer.password:
            error_message = "Password Required!!!!"
        elif len(customer.password) < 6:
            error_message = "Password length must be 6 charater or more."
        elif customer.isExists():
            error_message = "Email Already registered!!!!"
        return error_message
