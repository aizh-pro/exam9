# Generated by Django 2.2.13 on 2020-10-24 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20201024_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='photo',
        ),
        migrations.AddField(
            model_name='favorites',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='webapp.Photo', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]