from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Free

class FreeListView(ListView):
    model = Free
    paginate_by = 10
    template_name = 'free/free_list.html'  
    context_object_name = 'free_list'        #DEFAULT : <model_name>_list

    def get_queryset(self):
        free_list = Free.objects.order_by('-id') 
        return free_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context