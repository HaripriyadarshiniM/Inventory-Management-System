from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Supplier, Category
from .forms import ProductForm, SupplierForm
# Create your views here.

def home(request):
    category_name = request.GET.get('category')

    if category_name:
        products = Product.objects.filter(category__name__iexact=category_name)
    else:
        products = Product.objects.filter(quantity_in_stock__lte=10)

    return render(request, 'home.html', {
        'products': products,
        'category_name': category_name
    })


def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products':products})

def product_detail(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return render(request,'product_detail.html',{'product':product})
    return redirect('product-list')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request,'product_form.html', {'form':form})


def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request,'supplier_list.html',{'suppliers':suppliers})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier-list')
    else:
        form = SupplierForm()

    return render(request,'supplier_form.html',{'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request,'category_list.html',{'categories':categories})

