# Generated by Django 3.2.8 on 2021-10-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_website', '0003_auto_20211009_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='data_imgs/uploads'),
        ),
    ]
