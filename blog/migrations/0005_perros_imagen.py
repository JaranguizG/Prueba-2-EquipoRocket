# Generated by Django 2.1.2 on 2018-10-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_perros_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='perros',
            name='imagen',
            field=models.ImageField(default=123, upload_to=''),
            preserve_default=False,
        ),
    ]