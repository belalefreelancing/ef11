from django.shortcuts import render,redirect
from ef11_app.models import Banner
from .forms import *
# Create your views here.

def dashboardhome(request):
    banner = Banner.objects.all()
    return render(request, 'functionbase_crudapp/home.html', {'banner':banner})

def detail_view(request,pk):
    banner = Banner.objects.get(pk=pk)

    return render(request, 'functionbase_crudapp/detail.html', {'banner':banner})

def banner_add(request):
    form = BannerForm()
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard-home')
    return render(request, 'functionbase_crudapp/add.html', {'form':form})


def banner_eidt(request,pk):
    banner = Banner.objects.get(pk=pk)
    form = BannerForm(instance=banner)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES,instance=banner)
        if form.is_valid():
            form.save()
            return redirect('dashboard-home')
    return render(request, 'functionbase_crudapp/add.html', {'form':form})

def delete(request,pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect('dashboard-home')