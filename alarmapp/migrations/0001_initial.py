# Generated by Django 2.2.3 on 2019-10-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weblink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, verbose_name='Username')),
                ('cmd', models.CharField(max_length=120, verbose_name='UserCommand')),
                ('url', models.CharField(max_length=200, verbose_name='Weburl')),
            ],
        ),
    ]