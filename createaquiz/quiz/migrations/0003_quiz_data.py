"""
User created migration file that will initialize the database with
quiz information, instead of starting with an empty database.
"""
from datetime import date
from django.db import migrations

QUIZZES = [
    {
        'name': 'Know Your Powerpuff Girls Quiz',
        'slug': 'know-your-powerpuff-girls',
        'description': """I am Mojo Jojo!! In order to defeat my arch enemies, the Powerpuff girls, I have created a quiz that helps me to remember important facts about them! You can learn about them too and join my evil forces!
MOJO JOJO MOJO JOJO!""",
        'pub_date': date(2019, 10, 29),
        'tags': ['powerpuff-girls', 'television'],
        'author': 'mojojojo',
    },
    {
        'name': 'I hate Turtles!',
        'slug': 'i-hate-turtles',
        'description': "Fuck the turtles",
        'pub_date': date(2019, 10, 29),
        'tags': ['tmnt', 'television'],
        'author': 'shredder',
    },
]


def add_quiz_data(apps, schema_editor):
    Quiz = apps.get_model('quiz', 'Quiz')
    Tag = apps.get_model('quiz', 'Tag')
    User = apps.get_model('auth', 'User')
    for quiz_dict in QUIZZES:
        quiz = Quiz.objects.create(
            name=quiz_dict['name'],
            slug=quiz_dict['slug'],
            description=quiz_dict['description'],
            author=User.objects.get(username=quiz_dict['author']),
        )
        quiz.pub_date = quiz_dict['pub_date']
        quiz.save()
        for tag_slug in quiz_dict['tags']:
            quiz.tags.add(Tag.objects.get(slug=tag_slug))


def remove_quiz_data(apps, schema_editor):
    Quiz = apps.get_model('quiz', 'Quiz')
    for quiz_dict in QUIZZES:
        quiz = Quiz.objects.get(slug=quiz_dict['slug'])
        quiz.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_tag_data'),
        ('user', '0002_user_data'),
    ]

    operations = [
        migrations.RunPython(add_quiz_data, remove_quiz_data)
    ]
