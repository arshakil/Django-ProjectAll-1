from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,View
from . models import Item,OrderItem,Order
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    all_prods = Item.objects.all()
    all_featured_Item = Item.objects.filter(price__gte='200')


    context = {
        'all_prods': all_prods,
        'all_featured_Item': all_featured_Item,
    }
    return render(request, 'eshop/index.html',context);

def contact(request):
    return render(request, 'eshop/contact.html');
def about(request):
    return render(request, 'eshop/about.html');

def register(request):
    return render(request, 'eshop/register.html');
def login(request):
    return render(request, 'eshop/account.html');
def checkout(request):
    return render(request, 'eshop/checkout.html');
def productList(request):
    return render(request, 'eshop/products.html');
    
def single_item(request,slug):
    context = {
        'all_prods' : Item.objects.all(),
        'Item': get_object_or_404(Item, slug=slug),
    }
    return render(request, 'eshop/single_item.html',context);
 

# cart begin

def add_to_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart OldCart.")
            return redirect('home')

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart NewCart.")
    return redirect('product')




def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect('product')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("home")

class OrderSummaryView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'eshop/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")

def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("home")