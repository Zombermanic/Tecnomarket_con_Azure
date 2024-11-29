from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required

# Create your views here.

def home(request):
    return render(request, "core/index.html")

@permission_required('core.add_product')
def agregar_producto(request):
    data= {
        'form': ProductForm()
    }

    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto guardado correctamente")
        form

    return render(request, "core/productos/agregar.html", data)

@permission_required('core.view_product')
def listar_productos(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, "core/productos/listar.html", data)

@permission_required('core.change_product')
def modificar_producto(request, id):
    product = get_object_or_404(Product, id=id)
    data = {
        'form' : ProductForm(instance=product)
    }
    
    if request.method == "POST":
        form = ProductForm(data=request.POST, files = request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto modificado correctamente")
        form

    return render(request, "core/productos/modificar.html", data)

@permission_required('core.delete_product')
def eliminar_producto(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()

    return redirect(to="listar_productos")

def registro(request):
    data ={
        'form' : CustomUserCreationForm()
    }

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado exitosamente")
            return redirect(to='home')
        form


    return render(request, "registration/registro.html", data)
