# Generated by Django 2.2 on 2021-06-22 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_server_last_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ['-last_check'], 'permissions': (('login_server', '登录服务器'),)},
        ),
    ]