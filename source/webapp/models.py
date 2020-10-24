from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='user_pics', verbose_name='фото')
    description = models.CharField(max_length=20, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='photos', verbose_name='Автор')

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фоточки'
        ordering = ['-created_at']


class Favorites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='photo_likes', verbose_name='Пользователь')
    photo = models.ForeignKey('webapp.Photo',on_delete=models.CASCADE, related_name='likes', verbose_name='Фото')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'