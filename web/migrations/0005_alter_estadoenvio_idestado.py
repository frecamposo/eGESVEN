# Generated by Django 5.1.4 on 2024-12-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_metodopago_idmetodopago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadoenvio',
            name='idestado',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]