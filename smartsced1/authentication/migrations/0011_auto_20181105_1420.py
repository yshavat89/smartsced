# Generated by Django 2.0 on 2018-11-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20181105_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='media/default-user.png', upload_to='media/user_image'),
        ),
    ]
