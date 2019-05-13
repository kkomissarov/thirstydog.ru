from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'