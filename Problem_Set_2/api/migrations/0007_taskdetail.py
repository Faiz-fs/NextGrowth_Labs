# Generated by Django 5.0.1 on 2024-07-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_remove_appdetails_status_remove_user_scrshot"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskDetail",
            fields=[
                ("taskid", models.AutoField(primary_key=True, serialize=False)),
                ("appid", models.IntegerField()),
                ("userid", models.IntegerField()),
                ("taskname", models.CharField(max_length=100)),
                ("appIcon", models.ImageField(upload_to="images/")),
            ],
        ),
    ]