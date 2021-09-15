# Generated by Django 3.0.10 on 2021-07-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shepherd', '0018_auto_20210630_2205'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='domainserverconnection',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('static_server__isnull', False), ('transient_server__isnull', True)), models.Q(('static_server__isnull', True), ('transient_server__isnull', False)), _connector='OR'), name='only_one_server'),
        ),
    ]