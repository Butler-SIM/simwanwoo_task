# Generated by Django 3.1.7 on 2023-06-08 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="상품명")),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="태그명"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="옵션명")),
                ("price", models.IntegerField(verbose_name="가격")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="option_set",
                        related_query_name="option",
                        to="shop.product",
                        verbose_name="상품",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="tag_set",
            field=models.ManyToManyField(blank=True, to="shop.Tag"),
        ),
    ]
