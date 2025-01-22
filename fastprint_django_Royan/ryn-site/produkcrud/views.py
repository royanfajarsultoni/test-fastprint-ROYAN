from django.shortcuts import redirect, render, get_object_or_404
from .forms import produkForm, editprodukForm, statusForm, editstatusForm, kategoriForm, editkategoriForm
from .models import produk, status, kategori

# Produk views here.
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
    return render(request, context)


# Status views here.
def statusFormView(request):
    form = statusForm()
    if request.method == 'POST':
        form = statusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstatus_url')
    template_name = 'produkcrud/status.html'
    context = {'form': form}
    return render(request, template_name, context)

def showstatusView(request):
    obj = status.objects.all()
    template_name = 'produkcrud/showstatus.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updatestatusView(request, f_id_status):
    obj =  get_object_or_404(status,id_status=f_id_status)
    form = editstatusForm(instance=obj)
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['id_status'] = obj.id_status
        form = statusForm(post_data, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showstatus_url')
    template_name = 'produkcrud/editstatus.html'
    context = {'form': form}
    return render(request, template_name, context)

def deletestatusView(request, f_id_status):
    obj = get_object_or_404(status,id_status=f_id_status)
    if request.method == 'POST':
        obj.delete()
        return redirect('showstatus_url')
    context = {'obj': obj}
    return render(request, context)


# Kategori views here.
def kategoriFormView(request):
    form = kategoriForm()
    if request.method == 'POST':
        form = kategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showkategori_url')
    template_name = 'produkcrud/kategori.html'
    context = {'form': form}
    return render(request, template_name, context)

def showkategoriView(request):
    obj = kategori.objects.all()
    template_name = 'produkcrud/showkategori.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updatekategoriView(request, f_id_kategori):
    obj =  get_object_or_404(kategori,id_kategori=f_id_kategori)
    form = editkategoriForm(instance=obj)
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['id_kategori'] = obj.id_kategori
        form = kategoriForm(post_data, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showkategori_url')
    template_name = 'produkcrud/editkategori.html'
    context = {'form': form}
    return render(request, template_name, context)

def deletekategoriView(request, f_id_kategori):
    obj = get_object_or_404(kategori,id_kategori=f_id_kategori)
    if request.method == 'POST':
        obj.delete()
        return redirect('showkategori_url')
    context = {'obj': obj}
    return render(request, context)