# Generated by Django 3.0.3 on 2020-06-11 13:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=30, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Post', verbose_name='Tagged Post')),
            ],
        ),
    ]
