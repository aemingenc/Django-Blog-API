# Generated by Django 4.0.3 on 2022-03-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comments_card_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]