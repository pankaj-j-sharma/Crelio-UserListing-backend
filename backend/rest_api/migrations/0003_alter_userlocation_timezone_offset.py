# Generated by Django 4.0.6 on 2022-07-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_alter_usercontact_id_alter_userinfo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='timezone_offset',
            field=models.CharField(max_length=100),
        ),
    ]