# Generated by Django 5.0 on 2023-12-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taskModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('taskmodel', models.ManyToManyField(to='taskModel.taskmodel')),
            ],
        ),
    ]
