# Generated by Django 2.2.7 on 2019-12-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=20)),
                ('precioProducto', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]