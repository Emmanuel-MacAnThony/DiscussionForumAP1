# Generated by Django 3.2.8 on 2021-10-27 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_likes_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_likes',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
