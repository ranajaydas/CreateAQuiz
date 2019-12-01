"""
User created migration file that will initialize the database with
tag information, instead of starting with an empty database.
"""
from django.db import migrations


TAGS = (
    # (tag name, tag slug),
    ('capitals', 'capitals'),
    ('geography', 'geography'),
    ('powerpuff girls', 'powerpuff-girls'),
    ('television', 'television'),
    ('tmnt', 'tmnt'),
    ('comics', 'comics'),
    ('avengers', 'avengers'),
    ('asia', 'asia'),
    ('mountains', 'mountains'),
    ('food', 'food'),
    ('video games', 'video-games'),
    ("dexters lab", 'dexters-lab'),
    ("books", 'books'),
)


def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('quiz', 'Tag')    # Fetches the historical model of Tag (instead of importing it)
    for tag_name, tag_slug in TAGS:
        Tag.objects.create(name=tag_name, slug=tag_slug)


def remove_tag_date(apps, schema_editor):
    Tag = apps.get_model('quiz', 'Tag')  # Fetches the historical model of Tag (instead of importing it)
    for _, tag_slug in TAGS:
        tag = Tag.objects.get(slug=tag_slug)
        tag.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_tag_data, remove_tag_date)
    ]
