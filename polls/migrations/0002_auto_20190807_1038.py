# Generated by Django 2.2.4 on 2019-08-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Samosval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomer', models.IntegerField(unique=True)),
                ('model', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]