# Generated by Django 5.0.4 on 2024-06-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['sort'], 'verbose_name': 'Category', 'verbose_name_plural': '9.Categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-date_created'], 'verbose_name': 'Contact', 'verbose_name_plural': '2.Contacts'},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['-date_created'], 'verbose_name': 'Session', 'verbose_name_plural': '1.Sessions'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
