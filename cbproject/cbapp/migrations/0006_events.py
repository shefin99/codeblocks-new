# Generated by Django 4.2.1 on 2023-05-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbapp', '0005_topic_room_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_name', models.CharField(max_length=200)),
                ('e_desc', models.TextField(blank=True, null=True)),
                ('e_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]