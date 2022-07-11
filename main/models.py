from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class MovieModel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField()
    body = RichTextField()
    age = models.PositiveSmallIntegerField()
    time = models.CharField(max_length=5)
    movie_reliased = models.PositiveSmallIntegerField()
    category = models.ManyToManyField(CategoryModel)
    is_active = models.BooleanField(default=False)
    is_part_of_banner = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

class ScheduleModel(models.Model):
    movie = models.ForeignKey(MovieModel,on_delete=models.RESTRICT)
    price = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.date} {self.time}'

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'