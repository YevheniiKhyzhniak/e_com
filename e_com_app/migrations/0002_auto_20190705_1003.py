# Generated by Django 2.2.2 on 2019-07-05 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_com_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Subscriber',
        ),
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'MySubscriber', 'verbose_name_plural': 'A lot of Subscribers'},
        ),
    ]
