from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse
from orders.models import Order
from .forms import OrderPaymentForm


# Create your views here.
def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_list_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderPaymentForm(request)