# Generated by Django 2.2.2 on 2019-11-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0006_shortlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postajob',
            name='field',
            field=models.CharField(max_length=20),
        ),
    ]
