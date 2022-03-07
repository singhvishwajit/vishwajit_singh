# Generated by Django 3.0.1 on 2022-03-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_portfoliodistribution'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_size', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='PortfolioDistribution',
        ),
    ]
