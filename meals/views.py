from django.shortcuts import render

# Create your views here.
from order.forms import UserNewOrderForm
import itertools
from .models import Meals , Category

def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()

    context = {
        'meal_list' : meal_list ,
        'categories' : categories ,
    }

    return render(request , 'Meals/list.html' , context)



def meal_detail(request ,*args,**kwargs):
    selected_product_id = kwargs['mealsId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
    meal_detail = Meals.objects.get(id=kwargs["mealsId"])


    context = {
        'meal_detail' : meal_detail,
        'new_order_form': new_order_form
        }

    return render(request , 'Meals/detail.html' , context)