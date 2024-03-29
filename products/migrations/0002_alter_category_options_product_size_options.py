# Generated by Django 4.2 on 2023-04-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='size_options',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
