# Generated by Django 3.1.14 on 2023-12-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('MiddleName', models.CharField(max_length=200)),
                ('UserName', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]