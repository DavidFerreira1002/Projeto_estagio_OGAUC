# Generated by Django 3.2.5 on 2021-09-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_data', '0008_auto_20210915_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solar_image',
            name='CN_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='CNspots_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='DOP_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='HAZ_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='HA_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K1_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K3_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
        migrations.AlterField(
            model_name='solar_image',
            name='K3fac_image',
            field=models.ImageField(null=True, upload_to='2021_09_15_23_46'),
        ),
    ]
