# Generated by Django 3.1.5 on 2021-02-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20210207_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['order_no']},
        ),
        migrations.AddField(
            model_name='location',
            name='order_no',
            field=models.SmallIntegerField(default=0),
        ),
    ]