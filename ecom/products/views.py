from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    if request.method == 'GET':
        #display a list of all products
        products = Product.objects.all()
        return render(request, 'products/products_list.html', {'products': products})

    elif request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']

        new_product = Product(name=name, price=price, description=description, image=image)

        new_product.save()

        return redirect('product_list')

