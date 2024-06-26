# Generated by Django 4.1.13 on 2024-03-30 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webscrape_data', '0006_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Name', max_length=100)),
                ('email', models.EmailField(default='Email', max_length=254)),
                ('password', models.CharField(default='Password', max_length=100)),
                ('phone', models.CharField(default='Phone', max_length=15)),
                ('university_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(default='Email', max_length=254),
        ),
        migrations.AddField(
            model_name='vendor',
            name='name',
            field=models.CharField(default='Name', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='password',
            field=models.CharField(default='Password', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='phone',
            field=models.CharField(default='Phone', max_length=15),
        ),
    ]
