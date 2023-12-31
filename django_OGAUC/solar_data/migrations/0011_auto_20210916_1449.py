# Generated by Django 3.2.5 on 2021-09-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_data', '0010_auto_20210915_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solar_image',
            name='CN_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='CNspots_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='DOP_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='HAZ_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='HA_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K1_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K3_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K3fac_image',
            field=models.ImageField(null=True, upload_to='solar/2021_09_16_14_49'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='date',
            field=models.CharField(default='2021_09_16_14_49', max_length=20, null=True),
        ),
    ]
