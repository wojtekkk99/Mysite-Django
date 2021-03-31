# Generated by Django 3.1.6 on 2021-03-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
