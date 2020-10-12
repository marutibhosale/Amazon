# Generated by Django 3.0.4 on 2020-10-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RESOURCE', models.IntegerField()),
                ('MGR_ID', models.IntegerField()),
                ('ROLE_ROLLUP_1', models.IntegerField()),
                ('ROLE_ROLLUP_2', models.IntegerField()),
                ('ROLE_DEPTNAME', models.IntegerField()),
                ('ROLE_TITLE', models.IntegerField()),
                ('ROLE_FAMILY_DESC', models.IntegerField()),
                ('ROLE_FAMILY', models.IntegerField()),
            ],
        ),
    ]
