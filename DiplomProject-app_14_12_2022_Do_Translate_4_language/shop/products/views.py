from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm


def index(request, category_slug=None):


    context = {
        'title': 'Shop device',
        'categories': Category.objects.all(),
        'products': Product.objects.all(),

    }
    if category_slug:
        index = Product.objects.filter(category_id=category_slug)
    else:

        products = Product.objects.all()

    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    search_query = request.GET.get("search", "")

    context = {
        'title': 'Shop device - Каталог',
        'categories': Category.objects.all(),

    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        if search_query:
            products = Product.objects.filter(
                Q(name__icontains=search_query) |
                Q(short_description__icontains=search_query))
        else:
            products = Product.objects.all()

    paginator = Paginator(products, 6)  # Show 3 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'products': page_obj})
    return render(request, 'products/products.html', context)


def product_list(request, category_slug=None):

    category = None
    categories = Category.objects.all()
    products = Product.objects.all()  # filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,

                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
