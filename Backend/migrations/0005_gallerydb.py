# Generated by Django 4.1.5 on 2023-01-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_alter_ticketdb_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallerydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile/')),
            ],
        ),
    ]