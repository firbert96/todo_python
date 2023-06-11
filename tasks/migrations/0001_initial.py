# Generated by Django 3.2.11 on 2023-06-11 05:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('task_finished', models.BooleanField(default=True)),
                ('category', models.CharField(choices=[('DEFAULT', 'DEFAULT'), ('PERSONAL', 'PERSONAL'), ('SHOPPING', 'SHOPPING'), ('WISHLIST', 'WISHLIST'), (' WORK', ' WORK')], default='DEFAULT', max_length=20)),
            ],
        ),
    ]
