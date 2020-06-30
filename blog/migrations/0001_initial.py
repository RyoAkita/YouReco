# Generated by Django 3.0.3 on 2020-06-03 06:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='Category')),
            ],
        ),
    ]
