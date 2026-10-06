from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from product.models import Product
from .models import Order, OrderItem


@login_required
def checkout(request):

    cart = request.session.get('cart', {})

    product_ids = cart.keys()

    products = Product.objects.filter(id__in=product_ids)

    cart_items = []

    for product in products:

        quantity = cart[str(product.id)]

        subtotal = product.price * quantity

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    total = sum(
        item['subtotal']
        for item in cart_items
    )

    if request.method == 'POST':

        order = Order.objects.create(
            user=request.user,
            total=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price
            )

        request.session['cart'] = {}
        request.session.modified = True

        return redirect('/order/confirmation/')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def order_confirmation(request):

    return render(request, 'order_confirmation.html')


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'order_history.html', {
        'orders': orders
    })


@login_required
def order_detail(request, order_id):

    order = Order.objects.get(
        id=order_id,
        user=request.user
    )

    return render(request, 'order_detail.html', {
        'order': order
    })