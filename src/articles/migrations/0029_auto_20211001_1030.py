# Generated by Django 3.2.6 on 2021-10-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0028_auto_20210930_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hodimmodel',
            name='ilmiy_darajasi',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='hodimmodel',
            name='oqigan_joyi',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
