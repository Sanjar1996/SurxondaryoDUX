# Generated by Django 3.2.6 on 2021-12-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0029_auto_20211001_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='date',
            field=models.DateField(),
        ),
    ]
