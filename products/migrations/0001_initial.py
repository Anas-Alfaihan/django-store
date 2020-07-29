# Generated by Django 3.0.7 on 2020-07-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
