# Generated by Django 4.2.3 on 2023-07-26 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_rename_department_departmentmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentmodel",
            name="stu_department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.departmentmodel",
            ),
        ),
    ]