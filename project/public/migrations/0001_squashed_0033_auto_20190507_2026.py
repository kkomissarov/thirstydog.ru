# Generated by Django 2.2 on 2019-05-07 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('public', '0001_initial'), ('public', '0002_sitesettings'), ('public', '0003_auto_20190423_1835'), ('public', '0004_sitesettings_mainpage_img'), ('public', '0005_auto_20190423_1954'), ('public', '0006_auto_20190423_2006'), ('public', '0007_remove_mainpagesettings_mainpage_button_link'), ('public', '0008_auto_20190423_2101'), ('public', '0009_auto_20190423_2117'), ('public', '0010_mainpagesettings_firstscreen_button_color'), ('public', '0011_mainpagesettings_firstscreen_button_hover_color'), ('public', '0012_sitesettings'), ('public', '0013_auto_20190427_1428'), ('public', '0014_auto_20190427_1455'), ('public', '0015_auto_20190427_1456'), ('public', '0016_auto_20190428_1336'), ('public', '0017_auto_20190501_1324'), ('public', '0018_auto_20190501_1419'), ('public', '0019_auto_20190501_1424'), ('public', '0020_category_active'), ('public', '0021_remove_category_activate'), ('public', '0022_auto_20190501_2014'), ('public', '0023_auto_20190504_1539'), ('public', '0024_auto_20190504_1815'), ('public', '0025_auto_20190504_1817'), ('public', '0026_subscriber'), ('public', '0027_auto_20190505_1506'), ('public', '0028_order'), ('public', '0029_order_product'), ('public', '0030_auto_20190507_1952'), ('public', '0031_auto_20190507_2020'), ('public', '0032_auto_20190507_2021'), ('public', '0033_auto_20190507_2026')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Символльный код')),
                ('seo_title', models.CharField(blank=True, max_length=200, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, max_length=400, verbose_name='SEO Description')),
                ('top_text', models.TextField(blank=True, max_length=2000, verbose_name='Верхний текст')),
                ('sort_name', models.CharField(blank=True, max_length=400)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child', to='public.Category', verbose_name='Родительское категория')),
                ('level', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True, help_text='Отключенные категории исчезают с сайта', verbose_name='Категория активна')),
                ('img', models.ImageField(blank=True, null=True, upload_to='category-photo/', verbose_name='Изображение (используется на главной)')),
                ('show_on_mainpage', models.BooleanField(default=False, verbose_name='Выводить на главной')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Infopage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название страницы')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='Символльный код')),
                ('content', models.TextField(max_length=3000, verbose_name='Содержание')),
                ('show_in_menu', models.BooleanField(default=False, verbose_name='Выводить в верхнем меню')),
                ('seo_title', models.CharField(blank=True, help_text='Это поле будет заголовком страницы в браузере. Очень важное поле для поисковых систем. Заполнять нужно с умом', max_length=200, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, help_text='Мета-описание. Пользователи его не видят, но поисковикам важно, чтобы оно было заполнено. Пустым оставлять можно, но не рекомендуется.', max_length=400, verbose_name='SEO Description')),
                ('active', models.BooleanField(default=True, help_text='Отключенные материалы исчезают с сайта', verbose_name='Материал активен')),
            ],
            options={
                'verbose_name': 'Информационная страница',
                'verbose_name_plural': 'Информационные страницы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('slug', models.SlugField(blank=True, help_text='Это адрес страницы. Если оставить поле пустым, он сгенерируется автоматически.', max_length=200, unique=True, verbose_name='Символьный код')),
                ('price', models.PositiveIntegerField(help_text='Целое число в рублях. Без копеек.', verbose_name='Цена')),
                ('seo_title', models.CharField(blank=True, help_text='Это поле будет заголовком страницы в браузере. Очень важное поле для поисковых систем. Заполнять нужно с умом', max_length=200, verbose_name='SEO Title')),
                ('seo_description', models.CharField(blank=True, help_text='Мета-описание. Пользователи его не видят, но поисковикам важно, чтобы оно было заполнено. Пустым оставлять можно, но не рекомендуется.', max_length=400, verbose_name='SEO Description')),
                ('text_description', models.TextField(blank=True, max_length=2000, verbose_name='Описание')),
                ('active', models.BooleanField(default=True, help_text='Отключенные товары исчезают с сайта', verbose_name='Товар включен')),
                ('breadcrumb_category', models.ForeignKey(help_text='В эту категорию товар будет вложен по хлебным крошкам', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_products', to='public.Category', verbose_name='Хлебные крошки')),
                ('categories', models.ManyToManyField(help_text='Товар будет выводиться в выбранных категориях', related_name='secondary_products', to='public.Category', verbose_name='Категории')),
                ('l_status', models.CharField(choices=[('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')], default='in_stock', max_length=50, verbose_name='L')),
                ('m_status', models.CharField(choices=[('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')], default='in_stock', max_length=50, verbose_name='M')),
                ('s_status', models.CharField(choices=[('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')], default='in_stock', max_length=50, verbose_name='S')),
                ('xl_status', models.CharField(choices=[('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')], default='in_stock', max_length=50, verbose_name='XL')),
                ('xs_status', models.CharField(choices=[('В наличии', 'В наличии'), ('Под заказ', 'Под заказ')], default='in_stock', max_length=50, verbose_name='XS')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='product-photo/')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='public.Product')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='MainpageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Title главной страницы')),
                ('description', models.CharField(blank=True, max_length=400, verbose_name='Description главной страницы')),
                ('firstscreen_title', models.CharField(blank=True, max_length=100, verbose_name='Заголовок на первом экране главной страницы')),
                ('firstscreen_text', models.TextField(blank=True, verbose_name='Текст на первом экране главной страницы')),
                ('firstscreen_img', models.ImageField(blank=True, upload_to='mainpage-background/', verbose_name='Бэкграунд первого экрана')),
                ('firstscreen_button_txt', models.CharField(blank=True, max_length=20, verbose_name='Надпись на кнопке')),
                ('about_img', models.ImageField(blank=True, upload_to='about-img/', verbose_name='Картинка блока О нас')),
                ('about_text', models.TextField(blank=True, verbose_name='Текст блока О нас')),
                ('about_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок блока О нас')),
                ('cat_text', models.CharField(blank=True, max_length=100, verbose_name='Текст блока категорий')),
                ('cat_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок блока категорий')),
                ('subscribe_text', models.TextField(blank=True, verbose_name='Текст блока подписки')),
                ('subscribe_title', models.CharField(blank=True, max_length=50, verbose_name='Заголовок блока подписки')),
                ('firstscreen_button_color', models.CharField(blank=True, max_length=6, verbose_name='Цвет кнопки (HEX)')),
                ('firstscreen_button_hover_color', models.CharField(blank=True, max_length=6, verbose_name='Цвет кнопки при наведении мыши (HEX)')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='logo/', verbose_name='Лого в шапке')),
                ('footer_mail', models.CharField(max_length=50, verbose_name='Почта в подвале')),
                ('footer_social', models.TextField(verbose_name='Ссылки на соцсети')),
                ('logo_width_desktop', models.IntegerField(verbose_name='Ширина логотипа десктоп(в px)')),
                ('logo_width_mobile', models.IntegerField(verbose_name='Ширина логотипа в мобильном меню(в px)')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Подписчик',
                'verbose_name_plural': 'Подписчики',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя заказчика')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время заявки')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('product', models.CharField(max_length=100, null=True, verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
