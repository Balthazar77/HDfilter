from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Filter, Category, Product


class TestView(ListView):

    template_name = 'base.html'
    context_object_name = 'category'
    model = Category

    def get_queryset(self):
        queryset = super(TestView,self).get_queryset()
        return queryset.filter().all()


# def test_view(request):
#     categories = Category.objects.get_categories_for_left_sidebar()
#     return render(request, 'base.html', {'categories': categories})
#
# def get_queryset():
#     return super().get_queryset()

class ProductDetailView(DetailView):
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_field = 'slug'
    model = Filter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related('category')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)
        context['category'] = self.get_categoryes()
        return context

    def get_categoryes(self):
        cats = Category.objects.filter().all()
        return cats


    # CT_MODEL_MODEL_CLASS = {
    #     'filter': Filter,
    #
    # }

    # def dispatch(self, request, *args, **kwargs):
    #     self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
    #     self.queryset = self.model._base_manager.all()
    #     return super().dispatch(request, *args, **kwargs)