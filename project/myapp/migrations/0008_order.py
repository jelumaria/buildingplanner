# Generated by Django 4.1.7 on 2023-05-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_plan_details_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('eq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.equipment')),
            ],
        ),
    ]
