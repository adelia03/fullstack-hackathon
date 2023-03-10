# Generated by Django 4.1.4 on 2023-01-25 10:21

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
                ('last_name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='children')),
                ('bio', models.TextField()),
                ('sum', models.IntegerField()),
                ('donated', models.IntegerField(default=0)),
                ('ostatok', models.IntegerField(null=True)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildrenHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='children_house')),
                ('bio', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('donated', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now=True)),
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
            name='NarsingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='narsing_house')),
                ('bio', models.TextField()),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('donated', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='pets')),
                ('bio', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('donated', models.IntegerField(default=0)),
                ('created_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Pet',
                'verbose_name_plural': 'Pets',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=70)),
                ('image', models.ImageField(null=True, upload_to='volunteer')),
            ],
        ),
    ]
