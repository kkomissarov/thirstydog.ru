from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product, Category, Order
from subscribers.models import Subscriber
from settings.models import MainpageSettings, SiteSettings, Infopage
from .forms import SubscribeForm, OrderForm
from django.contrib.sitemaps import Sitemap




class MainPage(View):

    def get(self, request):
        context = {
            'mainpage_settings': MainpageSettings.objects.first(),
            'site_settings': SiteSettings.objects.first(),
            'catalog_menu_items': Category.objects.filter(active=True),
            'top_menu_items': Infopage.objects.filter(active=True, show_in_menu=True),
            'category_showcase': Category.objects.filter(active=True, show_on_mainpage=True),
            'subscribe_form': SubscribeForm
        }

        return render(request, 'public/mainpage.html', context)




class ProductPage(DetailView):

    model = Product
    template_name = 'public/productpage.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        object = get_object_or_404(Product, slug=slug, active=True)
        return object

    def get_context_data(self, **kwargs):
        context = super(ProductPage, self).get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['catalog_menu_items'] = Category.objects.filter(active=True)
        context['top_menu_items'] = Infopage.objects.filter(active=True, show_in_menu=True)
        context['order_form'] = OrderForm
        return context






class CategoryPage(ListView):
    model = Product
    paginate_by = 12
    template_name = 'public/categorypage.html'


    def get_context_data(self, **kwargs):
        context = super(CategoryPage, self).get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['category'] = Category.objects.filter(slug=self.kwargs.get('slug')).first()
        context['catalog_menu_items'] = Category.objects.filter(active=True)
        context['top_menu_items'] = Infopage.objects.filter(active=True, show_in_menu=True)

        #noindex для страниц пагинации
        if 'page' in self.request.GET:
            context['is_noindex'] = True
        else:
            context['is_noindex'] = False

        #canonical для страниц с любыми параметрами
        allow_params = ('page', )
        other_params = list(set(self.request.GET) - set(allow_params))
        if len(other_params) > 0:
            context['has_canonical'] = True




        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        if Category.objects.filter(slug=slug, active=True):
            queryset = Product.objects.filter(categories__slug=slug, active=True)
            return queryset
        else:
            raise Http404



class InfoPage(DetailView):
    model = Infopage
    template_name = 'public/infopage.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        object = get_object_or_404(Infopage, slug=slug, active=True)
        return object


    def get_context_data(self, **kwargs):
        context = super(InfoPage, self).get_context_data(**kwargs)
        context['site_settings'] = SiteSettings.objects.first()
        context['catalog_menu_items'] = Category.objects.filter(active=True)
        context['top_menu_items'] = Infopage.objects.filter(active=True, show_in_menu=True)
        return context



class SubscribeView(View):
    def post(self, request):
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            subscribe_data = subscribe_form.cleaned_data
            try:
                new_subscriber = Subscriber.objects.create(**subscribe_data)
                response = {
                    'status': 'success',
                    'message': 'Подписка успешно офорлмена'
                }

            except:
                response = {
                    'status': 'error',
                    'message': 'Не удалось оформить подписку. Возможно, такой подписчик уже существует'
                }


        else:
            response = {
                'status': 'error',
                'message': 'Не удалось оформить подписку. Возможно, вы указали email некорректно.'
            }

        return JsonResponse(response)



class OrderView(View):
    def post(self, request):
        order_form = OrderForm(request.POST)

        if order_form.is_valid():

            order_data = order_form.cleaned_data
            new_order = Order.objects.create(**order_data)
            return HttpResponse('Заявка успешно оформлена')


        else:
            return HttpResponse('Форма не валидна')





def page404(request, exception=None):
    return render(request, 'public/404.html', status=404)

