# Generated by Django 2.0.2 on 2018-02-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180217_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
