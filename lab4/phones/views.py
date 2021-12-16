from django.views import generic
from .models import Phone

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'phone_list'

    def get_queryset(self):
        return Phone.objects.order_by('-model_name')[:3]

class DetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Phone
