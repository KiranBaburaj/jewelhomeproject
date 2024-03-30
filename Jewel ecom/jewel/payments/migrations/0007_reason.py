# Generated by Django 5.0.2 on 2024-03-18 06:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_rating'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('Customer changed mind', 'Customer changed mind'), ('Delivery delay', 'Delivery delay'), ('Wrong size/color ordered', 'Wrong size/color ordered'), ('Duplicate order', 'Duplicate order'), ('Other', 'Other')], max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order')),
            ],
        ),
    ]
