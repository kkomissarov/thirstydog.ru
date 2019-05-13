from django.contrib.sitemaps import Sitemap
from .models import Product, Category
from settings.models import Infopage


class ProductSitemap(Sitemap):

    changefreq = 'always'
    priority = 1.0

    def items(self):
        return Product.objects.filter(active=True)


class CategorySitemap(Sitemap):

    changefreq = 'always'
    priority = 1.0

    def items(self):
        return Category.objects.filter(active=True)


class InfopageSitemap(Sitemap):

    changefreq = 'always'
    priority = 0.8

    def items(self):
        return Infopage.objects.filter(active=True)



sitemaps = {
    'product_sitemap': ProductSitemap,
    'category_sitemap': CategorySitemap,
    'infopage_sitemap': InfopageSitemap,
}

