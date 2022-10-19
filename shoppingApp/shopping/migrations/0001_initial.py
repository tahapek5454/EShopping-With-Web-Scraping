# Generated by Django 3.2.15 on 2022-10-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=50)),
                ('modelAdi', models.CharField(max_length=50)),
                ('modelNo', models.CharField(max_length=50)),
                ('isletimSistemi', models.CharField(max_length=50)),
                ('islemciTipi', models.CharField(max_length=50)),
                ('islemciNesli', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('diskBoyutu', models.CharField(max_length=50)),
                ('diskTuru', models.CharField(max_length=50)),
                ('ekranBoyu', models.CharField(max_length=50)),
                ('puani', models.CharField(max_length=5)),
                ('fiyat', models.DecimalField(decimal_places=2, max_digits=8)),
                ('prodLink', models.CharField(max_length=300)),
                ('imageLink', models.CharField(max_length=300)),
                ('prodTitle', models.CharField(max_length=300)),
                ('site', models.CharField(max_length=50)),
            ],
        ),
    ]