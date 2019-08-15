# Generated by Django 2.2.4 on 2019-08-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0011_auto_20190814_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinformation',
            name='PoolQC',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('NA', 'No Pool')], help_text='Pool quality', max_length=2, null=True),
        ),
    ]