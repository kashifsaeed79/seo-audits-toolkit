# Generated by Django 3.0.6 on 2020-12-13 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extractor', '0005_auto_20201213_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractor',
            name='type_audit',
            field=models.CharField(blank=True, choices=[('HEADERS', 'Headers')], max_length=20),
        ),
    ]
