# Generated by Django 4.0.4 on 2022-08-11 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_message_id_alter_message_seen'),
        ('posts', '0011_alter_post_tags_alter_tag_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('count', models.IntegerField(default=1)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
