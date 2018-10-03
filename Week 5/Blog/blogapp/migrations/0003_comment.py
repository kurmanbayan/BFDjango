# Generated by Django 2.1.2 on 2018-10-03 15:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20181003_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('blog_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Blog')),
            ],
        ),
    ]
