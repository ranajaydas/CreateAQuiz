"""
User created migration file that will initialize the database with
user information, instead of starting with an empty database.
"""
import os
from django.db import migrations
from django.contrib.auth.hashers import make_password


password = make_password(os.environ.get('DJANGO_USER_PASS'))
USERS = [
    {
        'username': 'mojojojo',
        'password': password,
        'email': 'mojo@jojo.com'
    },
    {
        'username': 'shredder',
        'password': password,
        'email': 'shredder@paper.com'
    },
    {
        'username': 'dexter',
        'password': password,
        'email': 'dexter@lab.com'
    },
]


def add_user_data(apps, schema_editor):
    User = apps.get_registered_model('auth', 'User')
    for user_dict in USERS:
        user = User(
            username=user_dict['username'],
            password=user_dict['password'],
            email=user_dict['email'],
        )
        user.save()


def remove_user_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    for user_dict in USERS:
        user = User.objects.get(username=user_dict['username'])
        user.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('quiz', '0002_tag_data'),
    ]

    operations = [
        migrations.RunPython(add_user_data, remove_user_data)
    ]
