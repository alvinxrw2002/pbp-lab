from django.http import HttpResponse
from django.core import serializers
from multiprocessing import context
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang' : data_barang_wishlist,
    'nama' : 'Alvin Xavier Rakha Wardhana'
}

def show_wishlist(request):
    return render(request, "wishlist.html", context)

data = BarangWishlist.objects.all()

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
