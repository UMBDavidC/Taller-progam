# Generated by Django 4.2.5 on 2023-11-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonio',
            name='fecha',
        ),
        migrations.AddField(
            model_name='testimonio',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='testimonio',
            name='testimonio',
            field=models.TextField(max_length=2000),
        ),
    ]
