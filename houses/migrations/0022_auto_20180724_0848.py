# Generated by Django 2.0.1 on 2018-07-24 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0021_auto_20180724_0846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paid',
            old_name='name_of_accomodation',
            new_name='accomodation',
        ),
    ]
