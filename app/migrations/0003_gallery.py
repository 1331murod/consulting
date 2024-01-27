# Generated by Django 4.2.9 on 2024-01-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_our_advantages_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='gallery/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
