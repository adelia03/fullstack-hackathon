# Generated by Django 4.1.5 on 2023-01-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeless',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('quantity', models.IntegerField()),
                ('donated', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='children',
            name='donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='children_house',
            name='donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='narsing_house',
            name='donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pets',
            name='donated',
            field=models.IntegerField(default=0),
        ),
    ]