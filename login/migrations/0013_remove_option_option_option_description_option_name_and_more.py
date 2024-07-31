# Generated by Django 4.2.4 on 2024-07-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_rename_moods_test_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='option',
        ),
        migrations.AddField(
            model_name='option',
            name='description',
            field=models.CharField(default='default description', max_length=100),
        ),
        migrations.AddField(
            model_name='option',
            name='name',
            field=models.CharField(default='default name', max_length=50),
        ),
        migrations.AddField(
            model_name='option',
            name='type',
            field=models.CharField(default='default type', max_length=20),
        ),
        migrations.AddField(
            model_name='option',
            name='value',
            field=models.CharField(default='default value', max_length=100),
        ),
    ]