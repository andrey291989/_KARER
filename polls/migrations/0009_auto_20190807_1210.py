# Generated by Django 2.2.4 on 2019-08-07 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190807_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samosval',
            name='zapolnen',
            field=models.IntegerField(),
        ),
    ]
