# Generated by Django 4.0.4 on 2022-04-21 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookSection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
