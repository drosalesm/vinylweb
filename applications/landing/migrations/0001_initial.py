# Generated by Django 3.1.7 on 2022-10-06 03:23

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biografia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo')),
                ('desc_princ', models.CharField(blank=True, max_length=500, null=True, verbose_name='descripcion principal')),
                ('integrante_uno', models.CharField(blank=True, max_length=100, null=True, verbose_name='Integrante 1')),
                ('integrante_dos', models.CharField(blank=True, max_length=100, null=True, verbose_name='Integrante 2')),
                ('desc_prim', models.CharField(blank=True, max_length=500, null=True, verbose_name='descripcion integrante 1')),
                ('desc_seg', models.CharField(blank=True, max_length=500, null=True, verbose_name='descripcion integrante 2')),
                ('imagen_one', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 1')),
                ('imagen_two', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 2')),
                ('imagen_three', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen 3')),
            ],
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField(verbose_name='Numero Celular')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('facebook', models.CharField(max_length=500, verbose_name='Facebook')),
                ('instagram', models.CharField(max_length=500, verbose_name='Instagram')),
                ('youtube', models.CharField(max_length=500, verbose_name='Youtube')),
                ('whatsapp', models.CharField(blank=True, max_length=500, null=True, verbose_name='Whatsapp')),
                ('Direccion', models.CharField(max_length=500, verbose_name='Youtube')),
            ],
        ),
        migrations.CreateModel(
            name='en_vivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('fecha_grabacion', models.DateField(blank=True, null=True)),
                ('url', embed_video.fields.EmbedVideoField()),
            ],
        ),
        migrations.CreateModel(
            name='nav_bar_opt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('link_contenido', models.CharField(blank=True, max_length=100, null=True, verbose_name='Palabra Link de contenido')),
                ('posicion', models.IntegerField(verbose_name='Posicion en navegador')),
            ],
        ),
        migrations.CreateModel(
            name='tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('tipo', models.CharField(choices=[('0', 'Cancion'), ('1', 'Beat'), ('2', 'Instrumental')], max_length=500, verbose_name='Tipo')),
                ('lanzamiento', models.DateField(null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen')),
                ('pista', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
