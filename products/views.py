from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "products/index.html")

def electronic(request):
    return render(request, "products/electronic.html")

def fashion(request):
    return render(request, "products/fashion.html")

def jewellery(request):
    return render(request, "products/jewellery.html")