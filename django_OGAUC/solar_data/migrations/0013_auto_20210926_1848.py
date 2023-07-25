# Generated by Django 3.2.5 on 2021-09-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_data', '0012_auto_20210920_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solar_image',
            name='CN_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='CNspots_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='DOP_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='HAZ_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='HA_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K1_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K3_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K3fac_image',
            field=models.ImageField(null=True, upload_to='solarData/2021_09_26_18_48'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='date',
            field=models.CharField(default='2021_09_26_18_48', max_length=20, null=True),
        ),
    ]