# Generated by Django 5.1 on 2024-09-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0057_user_entitlements"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="entitlements",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="stripe_customer_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
