from django.contrib import admin

from .models import MainpageSettings, SiteSettings, Infopage

class MainpageSettingsAdmin(admin.ModelAdmin):

    fieldsets = (

        ('Первый экран', {
            'fields': ('firstscreen_title', 'firstscreen_text', 'firstscreen_img', 'firstscreen_button_txt',
            'firstscreen_button_color', 'firstscreen_button_hover_color')
        }),

        ('Блок «Категории одежды»', {
            'fields': ('cat_title', 'cat_text')
        }),

        ('Блок «О нас»', {
            'fields': ('about_title', 'about_text', 'about_img')
        }),

        ('Блок «Подписки»', {
            'fields': ('subscribe_title', 'subscribe_text')
        }),

        ('SEO-информация', {
            'fields': ('title', 'description')
        }),

    )

    #Запрет на созданее второго экземпляра настроек
    def has_add_permission(self, request):

        count = MainpageSettings.objects.all().count()

        if count == 0:
            return True
        else:
            return False


    # Запрет на удаление экземпляра настроек
    def has_delete_permission(self, request, obj=None):
        return False


class SiteSettingsAdmin(admin.ModelAdmin):

    #Запрет на созданее второго экземпляра настроек
    def has_add_permission(self, request):

        count = SiteSettings.objects.all().count()

        if count == 0:
            return True
        else:
            return False

    # Запрет на удаление настроек
    def has_delete_permission(self, request, obj=None):
        return False



class InfopageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'slug', 'content', 'show_in_menu', 'active')
        }),


        ('SEO', {
            'fields': ('seo_title', 'seo_description'),
        }),

    )





admin.site.register(MainpageSettings, MainpageSettingsAdmin)
admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Infopage, InfopageAdmin)
