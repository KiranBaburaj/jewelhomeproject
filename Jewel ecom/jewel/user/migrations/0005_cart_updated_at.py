# Generated by Django 5.0.2 on 2024-02-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]