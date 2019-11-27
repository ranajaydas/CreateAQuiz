"""
User created migration file that will initialize the database with
quiz information, instead of starting with an empty database.
"""
from datetime import date
from django.db import migrations

QUIZZES = [
    {
        'name': 'Know Your Powerpuff Girls Quiz!',
        'slug': 'know-your-powerpuff-girls',
        'description': """I am Mojo Jojo!! In order to defeat my arch enemies, the Powerpuff girls, I have created a quiz that helps me to remember important facts about them! You can learn about them too and join my evil forces!
\nMOJO JOJO MOJO JOJO!""",
        'pub_date': date(2019, 10, 29),
        'tags': ['powerpuff-girls', 'television'],
        'author': 'mojojojo',
    },
    {
        'name': 'The Teenage Mutant Ninja Turtles Quiz!',
        'slug': 'tmnt-quiz',
        'description': "I am The Shredder! I came here to knit capes and make quizzes...and I'm all outta yarn!",
        'pub_date': date(2019, 10, 28),
        'tags': ['tmnt', 'television'],
        'author': 'shredder',
    },
    {
        'name': 'The Capitals of Asia Quiz',
        'slug': 'capitals-of-asia',
        'description': "I am The Shredder! Wait, I already declared that in my last quiz...\nANYWAY!\nThis quiz will test you on my home continent, Asia, and its capital cities!",
        'pub_date': date(2019, 10, 30),
        'tags': ['asia', 'capitals', 'geography'],
        'author': 'shredder',
    },
    {
        'name': 'The Mountains of the World Quiz',
        'slug': 'mountains-of-the-world',
        'description': "Here's a quiz to test your knowledge about the mountains of the world!",
        'pub_date': date(2019, 10, 27),
        'tags': ['geography', 'mountains'],
        'author': 'mojojojo',
    },
    {
        'name': 'Food Around The World Quiz',
        'slug': 'food-around-the-world',
        'description': "I AM THE SHR...\n\nYou thought I was going to say SHREDDER, didn't you?\n\nHere's a quiz to test your knowledge of the different cuisines of the world!",
        'pub_date': date(2019, 11, 1),
        'tags': ['food'],
        'author': 'shredder',
    },
    {
        'name': 'Video Games Quiz',
        'slug': 'video-games',
        'description': "Mojo Jojo loves playing video games! Now Mojo Jojo will test you!",
        'pub_date': date(2019, 11, 1),
        'tags': ['video-games'],
        'author': 'mojojojo',
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
