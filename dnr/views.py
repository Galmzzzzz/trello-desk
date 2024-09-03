from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Отображение всех заказов на главной странице
def main(request):
    orders = {
        'in_progress': Order.objects.filter(status='in_progress'),
        'ready_for_delivery': Order.objects.filter(status='ready_for_delivery'),
        'in_transit': Order.objects.filter(status='in_transit'),
        'completed': Order.objects.filter(status='completed'),
    }
    return render(request, 'dnr/main.html', {'orders': orders})

# Создание нового заказа через форму
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    return render(request, 'dnr/order.html', {'form': form})




