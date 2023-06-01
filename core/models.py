from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Page(models.Model):
    class Meta:
        abstract = True

    alias = models.SlugField("Урл страницы", max_length=200)
    seo_h1 = models.CharField("SEO H1", max_length=200, null=True, blank=True)
    seo_title = models.CharField("SEO Title", max_length=200, null=True, blank=True)
    seo_description = models.CharField("SEO description", max_length=500, null=True, blank=True)
    seo_keywords = models.CharField("SEO keywords", max_length=500, null=True, blank=True)
    content = RichTextField(verbose_name="Контент", config_name='default', null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)


class TextPage(Page):
    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    name = models.CharField("Название", max_length=200)
    menushow = models.BooleanField("Показывать в меню", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/' if self.alias == 'index' else f'/{self.alias}'


class News(Page):
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    name = models.CharField("Заголовок", max_length=200)
    photo = models.FileField('Фото', upload_to="news")
    dt_create = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    photo = models.FileField('Фото', upload_to="gallery")

    def __str__(self):
        return self.photo.name


class Review(models.Model):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    name = models.CharField("Имя", max_length=200)
    text = RichTextField(verbose_name="Контент", config_name='default', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    # клиент
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    comment = models.TextField('Комментарий', null=True, blank=True)
    dt_create = models.DateTimeField('Дата заявки', auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.dt_create}'
