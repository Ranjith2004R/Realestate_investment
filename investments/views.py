from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Investment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PropertyForm

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'investments/property_list.html', {'properties': properties})


def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    return render(request, 'investments/property_detail.html', {'property': property_obj})


def invest(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        Investment.objects.create(user=request.user, property=property_obj, amount_invested=amount)
        messages.success(request, 'Investment successful!')
        return redirect('property_list')
    return render(request, 'investments/invest.html', {'property': property_obj})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_list')  # Redirect to the property list view
    else:
        form = PropertyForm()
    
    return render(request, 'investments/add_property.html', {'form': form})
