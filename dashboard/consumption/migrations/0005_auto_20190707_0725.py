# Generated by Django 2.2.3 on 2019-07-07 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumption', '0004_auto_20190707_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consumption',
            old_name='avergae_consumption',
            new_name='average_consumption',
        ),
    ]