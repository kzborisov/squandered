# Generated by Django 4.0.3 on 2022-04-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_alter_income_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensecategory',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='incomecategory',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]