# Generated by Django 4.2.2 on 2023-07-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projects_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projects.tag'),
        ),
    ]
