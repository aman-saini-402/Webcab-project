# Generated by Django 3.0.4 on 2020-03-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='janta',
            old_name='first_name',
            new_name='outlook_id',
        ),
        migrations.RenameField(
            model_name='janta',
            old_name='last_name',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='janta',
            name='mob',
            field=models.CharField(max_length=10),
        ),
    ]