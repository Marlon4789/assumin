# Generated by Django 5.1.6 on 2025-02-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recording_emotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordingemotion',
            name='discovery',
            field=models.CharField(blank=True, max_length=300, verbose_name='¿Descubriste algo nuevo hoy?'),
        ),
    ]
