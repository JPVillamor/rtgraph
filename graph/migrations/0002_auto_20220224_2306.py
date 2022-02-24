# Generated by Django 3.2.12 on 2022-02-24 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='data_value',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='tool_used',
            field=models.CharField(max_length=200),
        ),
    ]
