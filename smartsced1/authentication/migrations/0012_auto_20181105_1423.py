# Generated by Django 2.0 on 2018-11-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20181105_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='user_image/default-user.png', upload_to='user_image'),
        ),
    ]
