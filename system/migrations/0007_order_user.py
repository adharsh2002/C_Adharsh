# Generated by Django 2.1 on 2022-02-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20220128_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]