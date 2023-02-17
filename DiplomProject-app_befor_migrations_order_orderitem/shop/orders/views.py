from django.shortcuts import render
from django.core.mail import send_mail

from .models import OrderItem
from .forms import OrderCreateForm
from products import basket_add, \
    basket_delete, DetailProduct


def order_create(request):
    cart = (basket_add(request), basket_delete(request), DetailProduct(request))
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            send_mail('Заказ оформлен',['alexsey@gmail.com'], fail_silently=False)
        return render(request, 'order/created.html',{'order':order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/create.html')
