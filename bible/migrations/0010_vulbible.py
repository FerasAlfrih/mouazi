# Generated by Django 3.0.8 on 2020-07-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0009_lxxbible'),
    ]

    operations = [
        migrations.CreateModel(
            name='VULBible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=5)),
                ('engName', models.CharField(max_length=300)),
                ('chapter', models.CharField(max_length=3)),
                ('verse', models.CharField(max_length=3)),
                ('text', models.TextField()),
            ],
        ),
    ]
