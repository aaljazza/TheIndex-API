# Generated by Django 2.0.2 on 2018-02-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='color',
            field=models.CharField(choices=[('R', 'red'), ('B', 'blue'), ('G', 'green'), ('Y', 'yellow'), ('K', 'black'), ('W', 'white'), ('Gr', 'grey')], default='W', max_length=2),
            preserve_default=False,
        ),
    ]
