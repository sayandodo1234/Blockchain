# Generated by Django 2.2.2 on 2019-07-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bchain', '0008_auto_20190711_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='prev_hash',
            field=models.CharField(default='00', editable=False, max_length=1000),
        ),
    ]
