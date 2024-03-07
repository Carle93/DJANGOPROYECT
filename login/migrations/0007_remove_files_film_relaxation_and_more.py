# Generated by Django 4.2.4 on 2024-03-07 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_moods_soft_delete_users_soft_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='film_relaxation',
        ),
        migrations.RemoveField(
            model_name='files',
            name='frequency_meditation',
        ),
        migrations.RemoveField(
            model_name='files',
            name='guided_meditation',
        ),
        migrations.RemoveField(
            model_name='files',
            name='moods',
        ),
        migrations.RemoveField(
            model_name='files',
            name='read_relaxation',
        ),
        migrations.AddField(
            model_name='files',
            name='location',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='files',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.test'),
        ),
        migrations.AddField(
            model_name='files',
            name='type',
            field=models.CharField(blank=True, choices=[('mp3', 'MP3'), ('mp4', 'MP4'), ('pdf', 'PDF')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='moods',
            name='category_moods',
            field=models.CharField(blank=True, choices=[('anxiety', 'Anxiety'), ('sadness', 'Sadness'), ('unmotivated', 'Unmotivated'), ('tiredness', 'Tiredness'), ('fear', 'Fear')], max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='Category_type_Test',
            field=models.CharField(blank=True, choices=[('Goldberg EADG', 'Test Axiety and Sadness'), ('EEP', 'Test Fear, Tiredness, Unmotivated')], max_length=13, null=True),
        ),
    ]