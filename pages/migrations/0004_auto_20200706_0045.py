# Generated by Django 3.0.7 on 2020-07-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200706_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(default='static/images/default.jpg', upload_to='static/images/'),
        ),
    ]