# Generated by Django 3.2.5 on 2021-07-26 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_auto_20210726_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='snscommentmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='snsmessagemodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]