from django.shortcuts import render
from .models import CD, Lib
from django.views.generic import UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy

def report(request):
    queryset = CD.objects.select_related('lib').all().order_by('name').order_by('lib') # select * from CD join Lib on CD.lib = lib.id
    disk_lib = {cds.lib: [cd for cd in queryset if (cds.lib.name == cd.lib.name)] for cds in queryset}

    return render(request, 'report.html', {'data':disk_lib})

class DetailCD(DetailView):
    model = CD
    template_name = 'detail.html'

class DeleteLib(DeleteView):
    model = Lib
    template_name = 'DeleteObj.html'
    success_url = reverse_lazy('CDLib:report')

class DeleteCD(DeleteView):
    model = CD
    template_name = 'DeleteObj.html'
    success_url = reverse_lazy('CDLib:report')

class UpdateLib(UpdateView):
    model = Lib
    template_name = 'UpdateObj.html'
    fields = ['name']

class UpdateCD(UpdateView):
    model = CD
    template_name = 'UpdateObj.html'
    fields = ['name', 'capacity', 'lib', 'cover']

class CreateLib(CreateView):
    model = Lib
    template_name = 'CreateObj.html'
    fields = ['name']

class CreateCD(CreateView):
    model = CD
    template_name = 'CreateObj.html'
    fields = ['name', 'capacity', 'lib', 'cover']
