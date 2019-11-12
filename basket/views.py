from django.shortcuts import render, reverse, redirect

# Create your views here.
def view_basket(request):
    return render(request, "basket.html")
    

def add_to_basket(request, id):
    quantity=int(request.POST.get('quantity'))
    
    basket = request.session.get('basket', {})
    basket[id] = basket.get(id, quantity)
    
    request.session['basket'] = basket
    return redirect(reverse('index'))
    
    
def update_basket(request, id):
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    
    if quantity > 0:
        basket[id] = quantity
    else:
        basket.pop[id]
        
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))