# Generated by Django 3.0.8 on 2020-10-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=True, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('phone_no', models.IntegerField()),
                ('profile_pic', models.ImageField(max_length=1024, upload_to='img/%Y/%m/%d/')),
            ],
        ),
    ]
