# Generated by Django 2.2.4 on 2019-10-14 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contentA', models.CharField(max_length=100)),
                ('contentB', models.CharField(max_length=100)),
                ('urlA', models.CharField(max_length=500)),
                ('urlB', models.CharField(max_length=500)),
                ('countA', models.IntegerField()),
                ('countB', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pepsi.Question')),
            ],
        ),
    ]