# Generated by Django 4.1 on 2023-04-20 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=200)),
                ("question_text", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("answer", models.CharField(max_length=200)),
                ("img_url", models.URLField(blank=True, null=True)),
                ("points", models.IntegerField(default=0)),
                ("difficulty", models.IntegerField(default=0)),
                ("category", models.CharField(default="General", max_length=200)),
                ("from_event", models.BooleanField(default=False)),
                ("event_name", models.CharField(blank=True, max_length=200, null=True)),
                ("event_url", models.URLField(blank=True, null=True)),
                ("tags", models.ManyToManyField(blank=True, to="cryptic.tag")),
            ],
        ),
        migrations.CreateModel(
            name="Additional_Hints",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hint_text", models.CharField(max_length=200)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cryptic.question",
                    ),
                ),
            ],
        ),
    ]
