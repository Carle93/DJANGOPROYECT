# Generated by Django 4.2.4 on 2023-12-09 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='User Name to Log In in the App', max_length=100)),
                ('email', models.EmailField(help_text='Email from the User in the App', max_length=100)),
                ('password', models.CharField(help_text='Password to enter in the App', max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]