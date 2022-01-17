# Generated by Django 4.0.1 on 2022-01-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating_chat', '0003_alter_client_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
    ]