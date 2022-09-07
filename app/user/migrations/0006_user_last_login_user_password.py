# Generated by Django 4.1 on 2022-09-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_usercommentlike_table_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(blank=True, null=True, verbose_name="last login"),
        ),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default="", max_length=128, verbose_name="password"),
            preserve_default=False,
        ),
    ]