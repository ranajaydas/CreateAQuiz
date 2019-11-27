"""
User created migration file that will initialize the database with
profile information, instead of starting with an empty database.
"""
from django.db import migrations

PROFILES = [
    {
        'name': 'Mojo Jojo',
        'slug': 'mojojojo',
        'about': 'Supreme evil monkey!\nArch nemesis of the Powerpuff girls\nPhilanthropist\nYoga enthusiast',
        'image': 'profile_pics/mojojojo.jpg',
    },
    {
        'name': 'The Shredder',
        'slug': 'shredder',
        'about': "The Shredder!\nI hate turtles!\nNot to be confused with the office appliance\nEven though I shred stuff\nApril O'Neil is...erm...cool and stuff\nFEAR ME!",
        'image': 'profile_pics/shredder.png',
    },
]


def add_profile_data(apps, schema_editor):
    Profile = apps.get_model('user', 'Profile')
    User = apps.get_model('auth', 'User')
    for profile_dict in PROFILES:
        profile = Profile.objects.create(
            user=User.objects.get(username=profile_dict['slug']),
            name=profile_dict['name'],
            slug=profile_dict['slug'],
            about=profile_dict['about'],
            image=profile_dict['image'],
        )
        profile.save()


def remove_profile_data(apps, schema_editor):
    Profile = apps.get_model('user', 'Profile')
    for profile_dict in PROFILES:
        profile = Profile.objects.get(slug=profile_dict['slug'])
        profile.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_data'),
    ]

    operations = [
        migrations.RunPython(add_profile_data, remove_profile_data)
    ]
