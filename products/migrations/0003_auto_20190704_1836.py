# Generated by Django 2.2.2 on 2019-07-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(null=True, upload_to='media/product_images'),
        ),
    ]