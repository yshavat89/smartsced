# Generated by Django 2.0 on 2018-11-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]
