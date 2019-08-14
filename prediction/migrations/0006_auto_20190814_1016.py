# Generated by Django 2.2.4 on 2019-08-14 09:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0005_auto_20190814_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinformation',
            name='FireplaceQu',
            field=models.CharField(choices=[('Ex', 'Excellent - Exceptional Masonry Fireplace'), ('Gd', 'Good - Masonry Fireplace in main level'), ('TA', 'Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement'), ('Fa', 'Fair - Prefabricated Fireplace in basement'), ('Po', 'Poor - Ben Franklin Stove')], help_text='Fireplace quality', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Fireplaces',
            field=models.IntegerField(default=0, help_text='Number of fireplaces (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
