# Generated by Django 4.0.6 on 2022-07-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_contatctmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.IntegerField(choices=[(1, 'Администрация'), (2, 'Отдел маркетинга'), (3, 'Жалобы и предложения'), (4, 'Отдел бухгалтерии'), (5, 'Отдел безопасности'), (6, 'Отдел чистоты')])),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=9)),
                ('gmail', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.DeleteModel(
            name='ContatctModel',
        ),
    ]