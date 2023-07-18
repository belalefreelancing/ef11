from django.shortcuts import render, redirect
# from .models import Banner,Product
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    banner = Banner.objects.all()
    product = Product.objects.all()
    elc_product = Product.objects.filter(category__name='Electronics')

    f_product = Product.objects.first()
    l_product = Product.objects.last()

    get_product = Product.objects.get(id=1)

    exact_product = Product.objects.filter(name__exact='Mohammad Belal Hossain')
    iexact_product = Product.objects.filter(name__iexact='mohammad belal HOssain')

    contains_product = Product.objects.filter(name__contains='h')
    # icontains_product = Product.objects.filter(name__icontains='Belal')

    gt_product = Product.objects.filter(price__gt=700)
    gte_product = Product.objects.filter(price__gte=665)

    lt_product = Product.objects.filter(price__lt=665)
    lte_product = Product.objects.filter(price__lte=665)


    print(lte_product)

    context = {
        'banner':banner,
        'product':product,
        'elc_product':elc_product,
        'f_product':f_product,
        'l_product':l_product,
        'get_product':get_product
    }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST,request.FIELS)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Submit')
            return redirect('contact')

    context ={
        'form':form
    }
    return render(request, 'contact.html',context)