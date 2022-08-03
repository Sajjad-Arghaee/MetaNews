# Generated by Django 4.0.4 on 2022-06-12 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('posts', '0004_post_author_post_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
