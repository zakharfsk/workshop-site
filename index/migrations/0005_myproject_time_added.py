# Generated by Django 4.1.1 on 2022-09-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_myjobexperience_time_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]