# Generated by Django 4.2.3 on 2023-10-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_crawledpages_content_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawledpages',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
