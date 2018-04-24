# Generated by Django 2.0.3 on 2018-04-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0004_auto_20180405_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knowlegefield',
            options={'ordering': ['order'], 'verbose_name': 'Область знаний', 'verbose_name_plural': 'Области знаний'},
        ),
        migrations.AlterModelOptions(
            name='process',
            options={'ordering': ['knowlege_field', 'process_group', 'order'], 'verbose_name': 'Процесс', 'verbose_name_plural': 'Процессы'},
        ),
        migrations.AlterModelOptions(
            name='processgroup',
            options={'ordering': ['order'], 'verbose_name': 'Группа процессов', 'verbose_name_plural': 'Группы процессов'},
        ),
        migrations.AddField(
            model_name='process',
            name='knowlege_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='process.KnowlegeField'),
        ),
        migrations.AlterField(
            model_name='process',
            name='process_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='process.ProcessGroup'),
        ),
    ]