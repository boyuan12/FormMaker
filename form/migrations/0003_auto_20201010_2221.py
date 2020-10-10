# Generated by Django 3.1.1 on 2020-10-10 22:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20201010_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inputfield',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
