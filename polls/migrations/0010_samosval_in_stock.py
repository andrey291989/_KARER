# Generated by Django 2.2.4 on 2019-08-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20190807_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='samosval',
            name='in_stock',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]