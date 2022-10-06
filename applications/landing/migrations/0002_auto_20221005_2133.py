# Generated by Django 3.1.7 on 2022-10-06 03:33

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracks',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='tracks',
            name='pista',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
