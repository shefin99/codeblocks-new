# Generated by Django 4.2.1 on 2023-05-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbapp', '0002_feature_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(max_length=200)),
                ('d_desc', models.TextField()),
            ],
        ),
    ]
