# Generated by Django 4.1.5 on 2023-01-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticketdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
                ('Rate', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]