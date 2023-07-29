# Generated by Django 4.2.3 on 2023-07-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buster', '0003_alter_rating_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='developers',
            field=models.ManyToManyField(related_name='games_deveopers', to='buster.developers', verbose_name='разработчик'),
        ),
        migrations.AddField(
            model_name='games',
            name='tagline',
            field=models.CharField(default='', max_length=100, verbose_name='Слоган'),
        ),
        migrations.AlterField(
            model_name='games',
            name='engine',
            field=models.CharField(max_length=100, verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='games',
            name='platforms',
            field=models.CharField(default='Windows', max_length=20, verbose_name='Платформа'),
        ),
        migrations.AlterField(
            model_name='games',
            name='preview',
            field=models.ImageField(upload_to='buster/', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='games',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название игры'),
        ),
        migrations.AlterField(
            model_name='games',
            name='year',
            field=models.PositiveSmallIntegerField(verbose_name='Дата выхода'),
        ),
    ]