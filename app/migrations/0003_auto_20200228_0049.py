# Generated by Django 3.0.3 on 2020-02-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200228_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='dish_desert',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='dish_main',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]