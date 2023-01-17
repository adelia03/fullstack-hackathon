# Generated by Django 4.1.5 on 2023-01-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('bio', models.TextField()),
                ('sum', models.IntegerField()),
                ('donated', models.IntegerField(default=0)),
                ('ostatok', models.IntegerField(null=True)),
                ('create', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Children_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('bio', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('donated', models.IntegerField(default=0)),
                ('create', models.DateField(auto_now=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='Narsing_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('bio', models.TextField()),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('donated', models.IntegerField(default=0)),
                ('create', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('bio', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('donated', models.IntegerField(default=0)),
                ('create', models.DateField(auto_now=True)),
            ],
        ),
    ]
