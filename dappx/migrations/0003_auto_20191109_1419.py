# Generated by Django 2.2.6 on 2019-11-09 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0002_blog_candidate_info_post_job'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post_job',
            new_name='postajob',
        ),
    ]
