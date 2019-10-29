# Generated by Django 2.2.6 on 2019-10-26 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('keebs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='builds', to=settings.AUTH_USER_MODEL),
        ),
    ]