# Generated by Django 5.0 on 2023-12-20 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinCen', '0003_asset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='user_id',
            new_name='user',
        ),
    ]
