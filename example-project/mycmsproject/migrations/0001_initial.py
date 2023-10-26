# Generated by Django 4.2.6 on 2023-10-26 23:43

from django.db import migrations, models
import django.db.models.deletion
import djangoplugins.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('djangoplugins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('plugin', djangoplugins.fields.PluginField(editable=False, limit_choices_to={'point__pythonpath': 'mycmsproject.plugins.ContentType'}, on_delete=django.db.models.deletion.CASCADE, to='djangoplugins.plugin')),
            ],
        ),
    ]