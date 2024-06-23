# Generated by Django 5.0.4 on 2024-06-22 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_banner_category_banner_subcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='category',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='main.category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='main.subcategory'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='main.category'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='main.subcategory'),
        ),
        migrations.AlterField(
            model_name='price',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.category'),
        ),
        migrations.AlterField(
            model_name='price',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.subcategory'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.category'),
        ),
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.category'),
        ),
        migrations.AlterField(
            model_name='services',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.subcategory'),
        ),
        migrations.AlterField(
            model_name='session',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='main.category'),
        ),
        migrations.AlterField(
            model_name='session',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='main.subcategory'),
        ),
    ]
