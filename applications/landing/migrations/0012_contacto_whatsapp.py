# Generated by Django 3.1.7 on 2022-10-02 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20221001_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Whatsapp'),
        ),
    ]
