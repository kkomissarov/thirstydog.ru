# Generated by Django 2.2 on 2019-05-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20190511_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='custom_html',
            field=models.TextField(blank=True, help_text='Сюда можно втставить коды счетчиков, кастомные скрипты и т.п.', null=True, verbose_name='Пользовательский код'),
        ),
    ]