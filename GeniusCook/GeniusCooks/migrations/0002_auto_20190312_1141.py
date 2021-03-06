# Generated by Django 2.1.2 on 2019-03-12 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeniusCooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='other', max_length=250),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='profile',
            field=models.ForeignKey(default='other', on_delete=django.db.models.deletion.CASCADE, to='GeniusCooks.Profile', unique=True),
        ),
    ]
