# Generated by Django 3.1.5 on 2021-03-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'MOBILE'), ('L', 'Laptop'), ('T', 'Tshirt')], default='M', max_length=2),
        ),
    ]