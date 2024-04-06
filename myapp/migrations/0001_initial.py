# Generated by Django 5.0.3 on 2024-03-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='Article/image')),
                ('create_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]