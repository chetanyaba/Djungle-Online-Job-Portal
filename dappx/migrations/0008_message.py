# Generated by Django 2.2.6 on 2019-11-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0007_auto_20191128_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('mess', models.TextField()),
            ],
        ),
    ]
