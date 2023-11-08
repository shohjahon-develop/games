# Generated by Django 4.2.6 on 2023-11-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remot_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='about/img')),
            ],
        ),
    ]
