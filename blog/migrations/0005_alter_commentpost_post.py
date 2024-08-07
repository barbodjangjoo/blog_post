# Generated by Django 5.0.7 on 2024-08-06 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_commentpost_datetime_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
