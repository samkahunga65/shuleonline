# Generated by Django 3.0.4 on 2020-05-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200505_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='done',
            field=models.IntegerField(default=0),
        ),
    ]