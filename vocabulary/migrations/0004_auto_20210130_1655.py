# Generated by Django 3.1.5 on 2021-01-30 15:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vocabulary', '0003_set_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studiedvocable',
            unique_together={('user', 'vocab')},
        ),
    ]
