# Generated by Django 2.2.4 on 2019-08-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0008_auto_20190814_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinformation',
            name='LotConfig',
            field=models.CharField(choices=[('Inside', 'Inside lot'), ('Corner', 'Corner lot'), ('CulDSac', 'Cul-de-sac'), ('FR2', 'Frontage on 2 sides of property'), ('FR3', 'Frontage on 3 sides of property')], help_text='Lot configuration', max_length=7, null=True),
        ),
    ]
