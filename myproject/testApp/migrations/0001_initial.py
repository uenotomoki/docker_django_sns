from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='SnsMessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('message', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='SnsCommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('snsmessagemodel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.snsmessagemodel')),
            ],
        ),
    ]
