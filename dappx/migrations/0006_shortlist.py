# Generated by Django 2.2.2 on 2019-11-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0005_candidate_info_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofemp', models.CharField(max_length=100)),
                ('name_of_company', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('stipend', models.IntegerField(default=None)),
            ],
        ),
    ]
