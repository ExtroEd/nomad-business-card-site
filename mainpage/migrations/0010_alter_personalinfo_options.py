# Generated by Django 5.1.2 on 2024-10-20 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_remove_additionalinfo_personal_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'Персональная информация', 'verbose_name_plural': 'Персональная информация'},
        ),
    ]