# Generated by Django 3.1.1 on 2020-10-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='question_id',
        ),
        migrations.AddField(
            model_name='form',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputfield',
            name='form_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
