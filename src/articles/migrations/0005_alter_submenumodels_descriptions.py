# Generated by Django 3.2.6 on 2021-08-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210811_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenumodels',
            name='descriptions',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
