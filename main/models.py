from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
# Create your models here.
BRANCHES = (
        (1,_('Администрация')),
        (2, _('Отдел маркетинга')),
        (3, _('Жалобы и предложения')),
        (4, _('Отдел бухгалтерии')),
        (5, _('Отдел безопасности')),
        (6, _('Отдел чистоты'))
    )

class ContactModel(models.Model):

    where = models.IntegerField(choices=BRANCHES)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)
    gmail = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

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