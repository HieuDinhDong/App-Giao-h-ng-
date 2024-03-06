# Generated by Django 4.0 on 2023-12-02 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id_driver', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='InfoDriver',
            fields=[
                ('id_info', models.AutoField(primary_key=True, serialize=False)),
                ('front_cccd', models.CharField(max_length=250)),
                ('behind_cccd', models.CharField(max_length=250)),
                ('front_license', models.CharField(max_length=250)),
                ('behind_license', models.CharField(max_length=250)),
                ('front_regis', models.CharField(max_length=250)),
                ('behind_regis', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('address_start', models.CharField(max_length=250)),
                ('address_end', models.CharField(max_length=250)),
                ('phone_receiver', models.CharField(max_length=250)),
                ('name_receiver', models.CharField(max_length=250)),
                ('price_ship', models.FloatField()),
                ('note', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOrder',
            fields=[
                ('id_type', models.AutoField(primary_key=True, serialize=False)),
                ('name_type', models.CharField(max_length=250)),
                ('describe', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OrderOfUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.driver')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='type_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.typeorder'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.user'),
        ),
        migrations.AddField(
            model_name='driver',
            name='info_driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.infodriver'),
        ),
        migrations.CreateModel(
            name='Commodities',
            fields=[
                ('id_com', models.AutoField(primary_key=True, serialize=False)),
                ('name_com', models.CharField(max_length=250)),
                ('describe_com', models.TextField()),
                ('weight', models.FloatField()),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.order')),
            ],
        ),
    ]