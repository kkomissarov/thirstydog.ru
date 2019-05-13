from django.contrib import admin

from .models import Product, ProductImage, Category, Order

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 10

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    list_display = ('name', 'price')
    search_fields = ('name',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'price', 'slug', 'text_description', 'active'),
        }),

        ('Связи', {
            'fields': ('breadcrumb_category', 'categories', ),
        }),

        ('Наличие', {
            'fields': ('xs_status', 's_status', 'm_status', 'l_status', 'xl_status', ),
        }),

        ('SEO', {
            'fields': ('seo_title', 'seo_description',),
        }),
    )
    filter_horizontal = ('categories',)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    exclude = ('level', 'sort_name',)
    ordering = ('sort_name', )
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'active', 'parent', 'sort_value'),
        }),

        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'top_text'),
        }),

        ('Вывод на главную страницу', {
            'fields': ('show_on_mainpage', 'img'),
        }),

    )



class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('name', 'phone', 'date', 'product')
    list_display = ('date', 'name', 'product')
    ordering = ('date', )

    fieldsets = (

        ('Заказчик', {
            'fields': ('name', 'phone')
        }),

        ('Заказ', {
            'fields': ('date', 'product')
        }),

        ('Дополнительно', {
            'fields': ('comment',)
        }),

    )

    # Не создавать заказы из админки
    def has_add_permission(self, request):
        return False


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)