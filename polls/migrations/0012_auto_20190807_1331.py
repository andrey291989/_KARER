# Generated by Django 2.2.4 on 2019-08-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20190807_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samosval',
            name='in_stock',
            field=models.IntegerField(db_index=True, default=5),
        ),
    ]
