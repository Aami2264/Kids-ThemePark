# Generated by Django 4.1.5 on 2023-02-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0010_alter_familyticketdb_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyticketdb',
            name='Amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
