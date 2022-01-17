from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from bazzar.models.customer import Customer
from bazzar.models.product import Product
from bazzar.models.orders import Order
from django.views import View


class CheckOut(View):
    def post(self,request):
       address = request.POST.get('address')
       phone = request.POST.get('phone')
       customer = request.session.get('customer')
       cart = request.session.get('cart')
       products = Product.get_products_by_id(list(cart.keys()))
       print(address, phone, customer, cart, products)

       for product in products:
           print(cart.get(str(product.id)))
           order = Order(customer = Customer(id = customer),
                         product = product,
                         price = product.price,
                         address = address,
                         phone = phone,
                         quantity = cart.get(str(product.id)))
           
           #print(order.placeOrder())
           order.save()
       request.session['cart'] = {}


       return redirect('cart')
    