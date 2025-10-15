from django.shortcuts import render, redirect , get_object_or_404 , HttpResponse
from .models import request_order
from .forms import Req_order

# Create your views here.
def request_order_view(request):
    if request.method == "POST" :
        form = Req_order(request.POST, request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('success-page')
    
    else :
        form = Req_order()
    return render(request, 'req_order.html', {'orders': form})

def listdisplay(request):
    list_orders = request_order.objects.all()
    return render(request, 'req_list.html' , {'orders': list_orders})

def success_page(request):
    return render(request, 'req_success.html')

def order_fulfilled(request, ord_id):
    order = get_object_or_404(request_order, pk = ord_id)

    if request.method == 'POST':
        order.delete()    
        return redirect('display-list')
    return render(request, 'confirm_fulfill.html', {'order': order})
        