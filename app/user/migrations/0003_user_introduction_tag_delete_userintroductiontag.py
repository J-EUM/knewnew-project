# Generated by Django 4.1 on 2022-08-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_rename_tag_userintroductiontag_introduction_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="introduction_tag",
            field=models.ManyToManyField(
                related_name="user", to="user.introductiontag"
            ),
        ),
        migrations.DeleteModel(
            name="UserIntroductionTag",
        ),
    ]
