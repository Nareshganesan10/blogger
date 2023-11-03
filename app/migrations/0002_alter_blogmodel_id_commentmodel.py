# Generated by Django 4.2.7 on 2023-11-03 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.blogmodel')),
            ],
        ),
    ]