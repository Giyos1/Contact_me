# Generated by Django 4.0.4 on 2022-04-21 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0002_alter_phonenumber_contact_alter_phonenumber_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
