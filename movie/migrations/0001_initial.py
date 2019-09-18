# Generated by Django 2.2.5 on 2019-09-13 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='movies/')),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('A', 'Action'), ('C', 'Comedy'), ('D', 'Drama'), ('R', 'Romance')], max_length=1)),
                ('year', models.DateField()),
                ('languages', models.CharField(choices=[('EN', 'English'), ('GE', 'German')], max_length=2)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
