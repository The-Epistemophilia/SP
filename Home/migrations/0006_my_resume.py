# Generated by Django 3.1.2 on 2021-02-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_about_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_7', models.CharField(max_length=200)),
            ],
        ),
    ]
