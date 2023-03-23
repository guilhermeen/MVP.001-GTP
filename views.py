from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Product, Category, Cart, CartItem, Order
from .forms import ProductForm, CategoryForm, CartForm, CartItemForm, OrderForm


class HomeView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


class CategoryListView(ListView):
    model = Category
    template_name = 'store/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    context_object_name = 'category'


class CartView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        cart_form = CartForm()
        cart_item_form = CartItemForm()
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            cart = Cart.objects.create(user=request.user)
        cart_items = cart.cartitem_set.all()
        total = sum(item.subtotal for item in cart_items)
        return render(request, 'store/cart.html', {'cart_form': cart_form,
                                                    'cart_item_form': cart_item_form,
                                                    'cart_items': cart_items,
                                                    'total': total})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()
        cart_form = CartForm(request.POST, instance=cart)
        cart_item_form = CartItemForm(request.POST)
        if cart_form.is_valid() and cart_item_form.is_valid():
            cart = cart_form.save(commit=False)
            cart.user = request.user
            cart.save()
            cart_item = cart_item_form.save(commit=False)
            cart_item.cart = cart
            cart_item.save()
        return redirect('cart')


class OrderView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        order_form = OrderForm()
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            return redirect('cart')
        cart_items = cart.cartitem_set.all()
        total = sum(item.subtotal for item in cart_items)
        return render(request, 'store/order.html', {'order_form': order_form,
                                                     'cart_items': cart_items,
                                                     'total': total})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST)
        cart = Cart.objects.filter(user=request.user).first()
        if order_form.is_valid() and cart:
            order = order_form.save(commit=False)
            order.user = request.user
            order.total = sum(item.subtotal for item in cart.cartitem_set.all())
            order.save()
            for item in cart.cartitem_set.all():
                item.order = order
                item.save()
            cart.delete()
        return redirect('home')


@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'store/product_form.html', {'form': form})


@login_required
def product_update(request, pk):
    product

def index(request):
    return render(request, 'index.html')