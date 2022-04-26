# Generated by Django 4.0.3 on 2022-04-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_task_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'слайд', 'verbose_name_plural': 'слайды'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='img',
        ),
        migrations.AddField(
            model_name='task',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='task',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='task',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
