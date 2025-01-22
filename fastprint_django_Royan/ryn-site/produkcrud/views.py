from django.shortcuts import redirect, render, get_object_or_404
from .forms import produkForm, editprodukForm
from .models import produk, status

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
    obj =  get_object_or_404(produk,id_produk=f_id_produk)
    form = editprodukForm(instance=obj)
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['id_produk'] = obj.id_produk
        form = produkForm(post_data, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showprod_url')
    template_name = 'produkcrud/editproduk.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_id_produk):
    obj = get_object_or_404(id_produk=f_id_produk)
    if request.method == 'POST':
        obj.delete()
        return redirect('showprod_url')
    context = {'obj': obj}
    return render(request, template_name, context)