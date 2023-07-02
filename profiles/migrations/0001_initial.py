# Generated by Django 4.2.2 on 2023-06-27 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=1000)),
                ('gender', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('birthdate', models.CharField(max_length=50)),
                ('place_of_birth', models.CharField(max_length=50)),
                ('marital_status', models.EmailField(max_length=50)),
                ('military_status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Personal Info',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('job_title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('Facebook', 'Facebook'), ('LinkedIn', 'LinkedIn'), ('Twitter', 'Twitter'), ('Discord', 'Discord'), ('Whatsapp', 'Whatsapp'), ('Telegram', 'Telegram'), ('Messanger', 'Messanger'), ('Instagram', 'Instagram')], default='Facebook', max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'verbose_name_plural': 'Social Links',
                'ordering': ['created_at'],
            },
        ),
    ]
