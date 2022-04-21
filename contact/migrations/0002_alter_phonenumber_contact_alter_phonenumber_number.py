# Generated by Django 4.0.4 on 2022-04-19 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='contact',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='contact.contact'),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
