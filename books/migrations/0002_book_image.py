# Generated by Django 5.0 on 2023-12-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]