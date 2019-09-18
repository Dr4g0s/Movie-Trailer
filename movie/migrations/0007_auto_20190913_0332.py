# Generated by Django 2.2.5 on 2019-09-13 03:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20190913_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('A', 'Action'), ('C', 'Comedy'), ('D', 'Drama'), ('R', 'Romance')], max_length=4),
        ),
    ]
