from django.shortcuts import render
from django.views import generic
from phones.models import Phone, Manufacturer

def mainView(request):
    return render(request, template_name='main.html')

class PhonesView(generic.ListView):
    context_object_name = 'phones'
    template_name = 'index.html'

    def get_queryset(self):
        return Phone.objects.all()

class ManufacView(generic.ListView):
    context_object_name = 'manufacs'
    template_name = 'index.html'

    def get_queryset(self):
        return Manufacturer.objects.all()

class PhoneDetail(generic.DetailView):
    template_name = 'detail.html'
    model = Phone

class ManufacDetail(generic.DetailView):
    template_name = 'detail.html'
    model = Manufacturer
