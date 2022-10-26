from datetime import datetime
from django.shortcuts import render, HttpResponse
from .models import Customer, Category, Product
from django.db.models import Q
 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_prod(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    print(context)
    return render(request, 'all_prod.html', context)

def add_prod(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        category_name = request.POST['category_name']
        price = int(request.POST['price'])
        
        new_prod = Product(product_name = product_name, category_name = category_name, price = price, purchase_date = datetime.now())
        new_prod.save()
        return HttpResponse('Product added Successfully')
    elif request.method=='GET':
        return render(request, 'add_prod.html')
    else:
        return HttpResponse("An Error Occured! Product Has Not Been Added")

def remove_prod(request, prod_id=0):
    if prod_id:
        try:
            prod_to_be_removed = Product.objects.get(id=prod_id)
            prod_to_be_removed.delete()
            return HttpResponse("Product Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Product id")
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'remove_prod.html',context)

def filter_prod(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        category_name = request.POST['category_name']
        price = request.POST['price']
        products = Product.objects.all()
        if product_name:
            products = products.filter(Q(product_name__icontains = product_name))
        if category_name:
            products = products.filter(category_name__icontains = category_name)
        if price:
            products = products.filter(price__icontains = price)

        context = {
            'products': products
        }
        return render(request, 'all_prod.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_prod.html')
    else:
        return HttpResponse('An Error Occurred')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        
        ins = Customer(name=name, email=email, phone=phone, desc=desc) # take the data from the user
        ins.save() # save it in the db
        print("The data has been saved to the database")
        
    return render(request, 'contact.html')