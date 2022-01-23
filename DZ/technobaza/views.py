from django.shortcuts import render
from django.views import generic
from technobaza.models import Phone
from django.db.models import Avg

class ListView(generic.ListView):
    context_object_name = 'phones'
    template_name = 'master.html'

    def get_queryset(self):
        return Phone.objects.all().order_by('manufacturer')

class DetailView(generic.DetailView):
    context_object_name = 'phone'
    template_name = 'detail.html'
    model = Phone

def reportView(request):
    avg_prices = Phone.objects.select_related('manufacturer')\
        .values('manufacturer__name')\
        .annotate(avg_price=Avg('price'))
    avg_prices = { el['manufacturer__name'] : el['avg_price'] for el in avg_prices}
    data = Phone.objects.select_related('manufacturer').values('id', 'model', 'manufacturer__name', 'price').order_by('id')
    return render(request, template_name='report.html', context={'avg_prices':avg_prices, 'data':data})
