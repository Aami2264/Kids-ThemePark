# Generated by Django 4.1.5 on 2023-02-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_alter_familyticketdb_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyticketdb',
            name='Amount',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]