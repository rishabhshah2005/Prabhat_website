# Generated by Django 3.2.8 on 2021-10-12 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_website', '0008_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='static/images/no_img.png', upload_to='data_imgs/uploads'),
        ),
    ]
