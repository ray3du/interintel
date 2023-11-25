from django.core.paginator import Paginator
from django.db.models import F, Count, Q
from django.http import JsonResponse
from django.views.generic import TemplateView, DetailView, ListView

from ecommerce.models import Product, Category


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    model = Product

    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page', 1)
        context = super().get_context_data(**kwargs)

        categories = (
            Category.objects.all()
            .annotate(count=Count(F('products')))
        )
        products_list = (
            self.model.objects.all()
            .select_related('category')
        )
        paginator = Paginator(products_list, 25)
        products = paginator.page(page)

        context["categories"] = categories
        context["products"] = products

        return context

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')

        if action:
            if action == "search_data":
                q = self.request.GET.get('q')
                query = Q(pk__isnull=False)
                if q:
                    query.add(Q(Q(name__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q)),
                              Q.AND)

                products = (
                               self.model.objects.filter(query)
                               .select_related('category')
                               .order_by('-id')
                           )[:10]

                return JsonResponse({
                    "results": [{
                        "id": product.id,
                        "name": product.name,
                        "description": product.description,
                        "category": {
                            "name": product.category.name
                        } if product.category is not None else {}
                    } for product in products]
                }, safe=False)

        return super().get(request, *args, **kwargs)


class ProductsView(ListView):
    model = Product
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', 1)

        categories = (
            Category.objects.all()
            .annotate(count=Count(F('products')))
        )

        products_list = context.get("object_list")

        paginator = Paginator(products_list, 25)
        products = paginator.page(page)

        context["categories"] = categories
        context["object_list"] = products
        print("context: ", context)
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = 'items_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = (
            Category.objects.all()
            .annotate(count=Count(F('products')))
        )

        product = context.get("object")
        """
            Get related products
        """
        products = (
                       Product.objects.filter(category=product.category)
                       .select_related('category')
                       .order_by('-id')
                   )[:4]

        context["categories"] = categories
        context["products"] = products

        return context
