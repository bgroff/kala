# Generated by Django 2.0.8 on 2018-11-21 03:35

import auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import django_localflavor_us.models
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '__first__'),
        ('auth', '0011_auto_20181002_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('timezone', timezone_field.fields.TimeZoneField(blank=True, default='UTC')),
                ('access_new_projects', models.BooleanField(default=False)),
                ('fax', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20, null=True)),
                ('home', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20, null=True)),
                ('mobile', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20, null=True)),
                ('office', django_localflavor_us.models.PhoneNumberField(blank=True, max_length=20, null=True)),
                ('ext', models.CharField(blank=True, max_length=10, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('removed', models.DateField(null=True)),
                ('avatar_url', models.URLField(max_length=1200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('organizations', models.ManyToManyField(to='organizations.Organization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
                'db_table': 'kala_user',
            },
            managers=[
                ('objects', auth.models.KalaUserManager()),
            ],
        ),
    ]
