# Generated by Django 4.0.3 on 2022-04-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_alter_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
