from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from meals.models import Meals
from order.models import orderDetail




# Create your views here.


@login_required
def add_user_order(request):
    count_product = int(request.POST.get("count"))
    product_ID = request.POST.get("product_id")
    product = Meals.objects.filter(id=product_ID).first()
    orderDetail.objects.create(name=product.slug, price=product.price, count=count_product)
    return redirect("/meals")




def order_list(request):
    count = 0
    for order in orderDetail.objects.all():
        count += (int(float(order.price)) * int(float(order.count)))

    context= {
        "orderlist" : orderDetail.objects.all(),
        "all_food":count
    }
    return render(request, "orderlist.html", context)
