from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Filter, Category


class TestView(ListView):

    template_name = 'base.html'
    context_object_name =
# def test_view(request):
#     categories = Category.objects.get_categories_for_left_sidebar()
#     return render(request, 'base.html', {'categories': categories})
#
# def get_queryset():
#     return super().get_queryset()

class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'filter': Filter,

    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    # model = Model
    # queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg =  'slug'