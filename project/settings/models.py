from django.db import models
from public.utils import gen_slug
from django.shortcuts import reverse

class MainpageSettings(models.Model):

    #SEO-информация
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Title главной страницы')

    description = models.CharField(
        max_length=400,
        blank=True,
        verbose_name='Description главной страницы')


    #Настройки первого экрана
    firstscreen_title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Заголовок на первом экране главной страницы')

    firstscreen_text = models.TextField(
        blank=True,
        verbose_name='Текст на первом экране главной страницы')

    firstscreen_img = models.ImageField(
        upload_to='mainpage-background/',
        blank=True,
        verbose_name='Бэкграунд первого экрана')

    firstscreen_button_txt = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Надпись на кнопке')

    firstscreen_button_color = models.CharField(
        max_length=6,
        blank=True,
        verbose_name='Цвет кнопки (HEX)'
    )

    firstscreen_button_hover_color = models.CharField(
        max_length=6,
        blank=True,
        verbose_name='Цвет кнопки при наведении мыши (HEX)'
    )

    #Настройки блока категорий
    cat_title = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Заголовок блока категорий')

    cat_text = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Текст блока категорий')

    #Настройки блока О нас
    about_title = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Заголовок блока О нас')

    about_text = models.TextField(
        blank=True,
        verbose_name='Текст блока О нас')

    about_img = models.ImageField(
        upload_to='about-img/',
        blank=True,
        verbose_name='Картинка блока О нас')

    #Настройки блока подписки
    subscribe_title = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Заголовок блока подписки')

    subscribe_text = models.TextField(
        blank=True,
        verbose_name='Текст блока подписки')

    def __str__(self):
        return 'Настройки главной страницы'

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'



#Общие настройки сайта
class SiteSettings(models.Model):

    logo = models.FileField(
        upload_to='logo/',
        verbose_name='Лого в шапке')

    logo_width_desktop = models.IntegerField(
        verbose_name='Ширина логотипа десктоп(в px)'
    )

    logo_width_mobile = models.IntegerField(
        verbose_name='Ширина логотипа в мобильном меню(в px)'
    )

    footer_mail = models.CharField(
        max_length=50,
        verbose_name='Почта в подвале'
    )

    footer_social = models.TextField(
        verbose_name='Ссылки на соцсети'
    )

    custom_html = models.TextField(
        verbose_name='Пользовательский код',
        help_text='Сюда можно втставить коды счетчиков, кастомные скрипты и т.п.',
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Общие настройки сайта'

    class Meta:
        verbose_name = 'Общие настройки сайта'
        verbose_name_plural = 'Общие настройки сайта'



class Infopage(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название страницы')

    slug = models.SlugField(
        max_length=200,
        blank=True,
        verbose_name='Символльный код',
        unique=True
    )

    content = models.TextField(
        max_length=3000,
        verbose_name='Содержание'
    )

    show_in_menu = models.BooleanField(
        verbose_name='Выводить в верхнем меню',
        default=False
    )

    active = models.BooleanField(
        default=True,
        verbose_name='Материал активен',
        help_text='Отключенные материалы исчезают с сайта')

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='SEO Title',
        help_text='Это поле будет заголовком страницы в браузере. Очень важное поле для поисковых систем. Заполнять нужно с умом',)

    seo_description = models.CharField(
        max_length=400,
        blank=True,
        verbose_name='SEO Description',
        help_text='Мета-описание. Пользователи его не видят, но поисковикам важно, чтобы оно было заполнено. Пустым оставлять можно, но не рекомендуется.')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info_page', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        #сгенирировать слаг, если он пустой или категория еще не создана
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = 'Информационные страницы'

