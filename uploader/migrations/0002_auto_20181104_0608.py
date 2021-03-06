# Generated by Django 2.1 on 2018-11-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='song',
            new_name='songfile',
        ),
        migrations.AddField(
            model_name='upload',
            name='album',
            field=models.CharField(default='foobar', max_length=40),
        ),
        migrations.AddField(
            model_name='upload',
            name='albumartist',
            field=models.CharField(default='foobar', max_length=30),
        ),
        migrations.AddField(
            model_name='upload',
            name='artist',
            field=models.CharField(default='foobar', max_length=100),
        ),
        migrations.AddField(
            model_name='upload',
            name='genre',
            field=models.CharField(default='foobar', max_length=20),
        ),
        migrations.AddField(
            model_name='upload',
            name='releaseyear',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='upload',
            name='songname',
            field=models.CharField(default='foobar', max_length=50),
        ),
        migrations.AddField(
            model_name='upload',
            name='tracknumber',
            field=models.IntegerField(default=0),
        ),
    ]
