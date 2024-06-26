# Generated by Django 4.2.3 on 2023-08-19 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CollegeUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=60, unique=True, verbose_name="email"),
                ),
                ("username", models.CharField(max_length=255, unique=True)),
                (
                    "privilege",
                    models.IntegerField(
                        choices=[
                            (0, "Superuser"),
                            (1, "Principal"),
                            (2, "HOD"),
                            (3, "Employee"),
                        ],
                        default=3,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "college_user",
            },
        ),
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "activity",
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("available_amount", models.IntegerField(default=0)),
                ("total_amount", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "department",
            },
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("item", models.TextField(blank=True, null=True)),
                ("requested_amount", models.IntegerField(default=0)),
                ("approved_amount", models.IntegerField(default=0)),
                ("file", models.FileField(blank=True, null=True, upload_to="uploads/")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("requested", "Requested"),
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="requested",
                        max_length=255,
                    ),
                ),
                ("note", models.TextField(blank=True, null=True)),
                ("request_date", models.DateTimeField(auto_now_add=True)),
                ("is_read_date", models.DateTimeField(blank=True, null=True)),
                ("approved_date", models.DateTimeField(blank=True, null=True)),
                ("rejected_date", models.DateTimeField(blank=True, null=True)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "activity",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="api.activity",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "transaction",
            },
        ),
        migrations.AddField(
            model_name="activity",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="activities",
                to="api.department",
            ),
        ),
        migrations.AddField(
            model_name="collegeuser",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="api.department",
            ),
        ),
        migrations.AddField(
            model_name="collegeuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="collegeuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
