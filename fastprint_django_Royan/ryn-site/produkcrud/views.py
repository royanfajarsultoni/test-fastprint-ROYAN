from django.shortcuts import redirect, render
from .forms import produkForm
from .models import produk

# Create your views here.
def produkFormView(request):
    form = produkForm()
    if request.method == 'POST':
        form = produkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showprod_url')
    template_name = 'produkcrud/produk.html'
    context = {'form': form}
    return render(request, template_name, context)

def showView(request):
    obj = produk.objects.all()
    template_name = 'produkcrud/showprod.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateView(request, f_id_produk):
    obj = produk.objects.get(id_produk=f_id_produk)
    form = produkForm(instance=obj)
    if request.method == 'POST':
        form = produkForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showprod_url')
    template_name = 'produkcrud/produk.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_id_produk):
    obj = produk.objects.get(id_produk=f_id_produk)
    if request.method == 'POST':
        obj.delete()
        return redirect('showprod_url')
    template_name = 'produkcrud/konfirmasi.html'
    context = {'obj': obj}
    return render(request, template_name, context)