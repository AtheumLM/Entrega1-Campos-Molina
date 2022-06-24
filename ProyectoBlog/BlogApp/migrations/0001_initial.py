# Generated by Django 4.0.5 on 2022-06-24 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rubro', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Pais', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('categorias_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='BlogApp.categorias')),
                ('Titulo', models.CharField(max_length=60)),
                ('Texto', models.CharField(max_length=500)),
            ],
            bases=('BlogApp.categorias',),
        ),
    ]
