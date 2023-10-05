# Generated by Django 4.2.5 on 2023-10-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProfitableTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата дохода')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Наименование дохода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание дохода')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Сумма')),
                ('income_type', models.ManyToManyField(blank=True, to='transaction.incometype', verbose_name='Тип дохода')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenditureTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата расхода')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Наименование расхода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание расхода')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Количество измерителя')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Цена за единицу измерения')),
                ('category', models.ManyToManyField(blank=True, to='transaction.category', verbose_name='Категория расхода')),
                ('meter', models.ManyToManyField(blank=True, to='transaction.meter', verbose_name='Единица измерения товара/услуги')),
            ],
        ),
    ]