from django.db import models
from django.urls import reverse
from .utils import gen_slug, get_sort_name, get_level


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название категории')

    slug = models.SlugField(
        max_length=200,
        blank=True,
        verbose_name='Символльный код',
        unique=True
    )

    active = models.BooleanField(
        default=True,
        verbose_name='Категория активна',
        help_text='Отключенные категории исчезают с сайта')

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='SEO Title'
    )

    seo_description = models.CharField(
        max_length=400,
        blank=True,
        verbose_name='SEO Description'
    )

    top_text = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name='Верхний текст'
    )

    parent = models.ForeignKey(
        'self',
        verbose_name='Родительское категория',
        null=True,
        blank=True,
        related_name='child',
        on_delete=models.DO_NOTHING)

    img = models.ImageField(
        verbose_name='Изображение (используется на главной)',
        blank=True,
        null=True,
        upload_to='category-photo/'
    )

    show_on_mainpage = models.BooleanField(
        verbose_name='Выводить на главной',
        default=False
    )


    level = models.PositiveIntegerField(
        default=0)

    sort_name = models.CharField(
        max_length=400,
        blank=True)

    sort_value = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Порядок сортировки',
        help_text='Чем меньше значение, тем раньше выводится категория в меню')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['sort_value']

    def __str__(self):
        return self.sort_name

    def get_absolute_url(self):
        return reverse('category_page', kwargs={'slug': self.slug})


    def get_all_parents(self):
        if self.level > 0:
            all_parents = []

            obj = self.parent
            for i in range(0, self.level):
                all_parents.append(obj)
                if i < self.level:
                    obj = obj.parent
            return all_parents

        else:
            return None


    def save(self, *args, **kwargs):
        #сгенирировать слаг, если он пустой или категория еще не создана
        if not self.slug:
            self.slug = gen_slug(self.name)

        #посчитать уровень вложенности
        self.level = get_level(self)

        #сгенерировать имя для сортировки, включающее все родительские категории
        self.sort_name = get_sort_name(self)
        super().save(*args, **kwargs)

        #Пересохранить все дочерние категории, чтобы перегенирировать их sort_name и пересчитать уровень вложенности
        if self.child.count() > 0:
            childs = self.child.all()

            for child in childs:
                child.save()




class Product(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        verbose_name='Название товара')

    slug = models.SlugField(
        max_length=200,
        blank=True,
        verbose_name='Символьный код',
        unique=True,
        help_text='Это адрес страницы. Если оставить поле пустым, он сгенерируется автоматически.')

    price = models.PositiveIntegerField(
        blank=False,
        verbose_name='Цена',
        help_text='Целое число в рублях. Без копеек.')

    breadcrumb_category = models.ForeignKey(
        Category,
        verbose_name='Хлебные крошки',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='main_products',
        help_text='В эту категорию товар будет вложен по хлебным крошкам'
        )

    categories = models.ManyToManyField(
        Category,
        verbose_name='Категории',
        related_name='secondary_products',
        help_text='Товар будет выводиться в выбранных категориях')


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

    text_description = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name='Описание')

    active = models.BooleanField(
        default=True,
        verbose_name='Товар включен',
        help_text='Отключенные товары исчезают с сайта')

    xs_status = models.CharField(
        choices=(('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')),
        verbose_name='XS',
        max_length=50,
        default='in_stock')

    s_status = models.CharField(
        choices=(('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')),
        verbose_name='S',
        max_length=50,
        default='in_stock')

    m_status = models.CharField(
        choices=(('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')),
        verbose_name='M',
        max_length=50,
        default='in_stock')

    l_status = models.CharField(
        choices=(('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')),
        verbose_name='L',
        max_length=50,
        default='in_stock')

    xl_status = models.CharField(
        choices=(('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')),
        verbose_name='XL',
        max_length=50,
        default='in_stock')

    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-pub_date']


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product_page', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)




class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='images',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    image = models.ImageField(
        upload_to='product-photo/',
        blank=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'





class Order(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя заказчика')

    phone = models.CharField(
        max_length=10,
        verbose_name='Телефон')

    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время заявки')

    product = models.CharField(
        max_length=100,
        null=True,
        verbose_name='Товар')

    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарий')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'