from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Developers(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Developers/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчик"

class Genre(models.Model):
    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Games(models.Model):
    title = models.CharField("Название игры", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    platforms = models.CharField("Платформа", max_length=20, default="Windows")
    engine = models.CharField("Двигатель", max_length=100)
    preview = models.ImageField("Превью", upload_to="buster/")
    developers = models.ManyToManyField(Developers, verbose_name="разработчик", related_name="games_deveopers")
    year = models.PositiveSmallIntegerField("Дата выхода")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в $")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class GamesShorts(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="games_shorts/")
    games = models.ForeignKey(Games, verbose_name="Игра", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из игры"
        verbose_name_plural = "Кадры из игры"

class TopReating(models.Model):
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Топ рейтинга"
        verbose_name_plural = "Топы рейтинга"

class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(TopReating, on_delete=models.CASCADE, verbose_name="топ")
    games = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name="игра")

    def __str__(self):
        return f"{self.star} - {self.games}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    games = models.ForeignKey(Games, verbose_name="игра", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.games}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"