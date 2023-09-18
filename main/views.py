from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.forms import Item

# Create your views here.
def show_main(request):
    items = Item.objects.all()
    context = {
        'name': 'Amanda Oktivia Sharfina',
        'class': 'PBP B',
        'items': items

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)