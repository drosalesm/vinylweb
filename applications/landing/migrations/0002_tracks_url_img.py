# Generated by Django 3.1.7 on 2022-10-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracks',
            name='url_img',
            field=models.URLField(blank=True, null=True),
        ),
    ]