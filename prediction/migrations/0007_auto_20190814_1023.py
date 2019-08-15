# Generated by Django 2.2.4 on 2019-08-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0006_auto_20190814_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinformation',
            name='BsmtFinType1',
            field=models.CharField(choices=[('GLQ', 'Good Living Quarters'), ('ALQ', 'Average Living Quarters'), ('BLQ', 'Below Average Living Quarters'), ('Rec', 'Average Rec Room'), ('LwQ', 'Low Quality'), ('Unf', 'Unfinshed'), ('NA', 'No Basement')], help_text='Rating of basement finished area', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='houseinformation',
            name='BsmtFinType2',
            field=models.CharField(choices=[('GLQ', 'Good Living Quarters'), ('ALQ', 'Average Living Quarters'), ('BLQ', 'Below Average Living Quarters'), ('Rec', 'Average Rec Room'), ('LwQ', 'Low Quality'), ('Unf', 'Unfinshed'), ('NA', 'No Basement')], help_text='Rating of basement finished area (if multiple types)', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='houseinformation',
            name='GarageType',
            field=models.CharField(choices=[('2Types', 'More than one type of garage'), ('Attchd', 'Attached to home'), ('Basment', 'Basement Garage'), ('BuiltIn', 'Built-In (Garage part of house - typically has room above garage)'), ('CarPort', 'Car Port'), ('Detchd', 'Detached from home'), ('NA', 'No Garage')], help_text='Garage location', max_length=6, null=True),
        ),
    ]