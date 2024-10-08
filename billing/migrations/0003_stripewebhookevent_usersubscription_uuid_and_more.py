# Generated by Django 5.1 on 2024-08-30 15:55

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0056_user_stripe_customer_id"),
        ("billing", "0002_subscriptionplan_stripe_price_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StripeWebhookEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event_id", models.CharField(max_length=100, unique=True)),
                ("event_type", models.CharField(max_length=100)),
                ("data", models.JSONField()),
                ("raw_event", models.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name="usersubscription",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.CreateModel(
            name="StripeCheckoutSession",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("stripe_session_id", models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ("features", models.ManyToManyField(related_name="checkout_sessions", to="billing.planfeature")),
                (
                    "organization",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="backend.organization"),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="checkout_sessions", to="billing.subscriptionplan"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "abstract": False,
                "constraints": [
                    models.CheckConstraint(
                        check=models.Q(
                            models.Q(("organization__isnull", False), ("user__isnull", True)),
                            models.Q(("organization__isnull", True), ("user__isnull", False)),
                            _connector="OR",
                        ),
                        name="billing_stripecheckoutsession_check_user_or_organization",
                    )
                ],
            },
        ),
    ]
