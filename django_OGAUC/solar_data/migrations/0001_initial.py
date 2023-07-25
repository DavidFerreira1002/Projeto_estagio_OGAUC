# Generated by Django 3.2.5 on 2021-09-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solar_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HA_image', models.ImageField(null=True, upload_to='media/')),
                ('HAZ_image', models.ImageField(null=True, upload_to=None)),
                ('CN_image', models.ImageField(null=True, upload_to=None)),
                ('CNspots_image', models.ImageField(null=True, upload_to=None)),
                ('DOP_image', models.ImageField(null=True, upload_to=None)),
                ('K1_image', models.ImageField(null=True, upload_to=None)),
                ('K3_image', models.ImageField(null=True, upload_to=None)),
                ('K3fac_image', models.ImageField(null=True, upload_to=None)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
