# Generated by Django 2.2.4 on 2019-08-14 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0010_auto_20190814_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houseinformation',
            old_name='ExterQaul',
            new_name='ExterQual',
        ),
        migrations.RenameField(
            model_name='houseinformation',
            old_name='RoofMtl',
            new_name='RoofMatl',
        ),
    ]
