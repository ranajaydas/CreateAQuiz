"""
User created migration file that will initialize the database with
quiz information, instead of starting with an empty database.
"""
from datetime import date
from django.db import migrations

max_image_size = (800, 800)

QUIZZES = [
    {
        'name': 'Know Your Powerpuff Girls Quiz!',
        'slug': 'know-your-powerpuff-girls',
        'description': """I am Mojo Jojo!! In order to defeat my arch enemies, the Powerpuff girls, I have created a quiz that helps me to remember important facts about them! You can learn about them too and join my evil forces!
\nMOJO JOJO MOJO JOJO!""",
        'pub_date': date(2019, 10, 29),
        'tags': ['powerpuff-girls', 'television'],
        'author': 'mojojojo',
        'image': 'quiz_headers/powerpuffgirls.jpg',
    },
    {
        'name': 'The Teenage Mutant Ninja Turtles Quiz!',
        'slug': 'tmnt-quiz',
        'description': "I am The Shredder! I came here to knit capes and make quizzes...and I'm all outta yarn!\n\n(Image courtesy of Lionsgate)",
        'pub_date': date(2019, 10, 28),
        'tags': ['tmnt', 'television'],
        'author': 'shredder',
        'image': 'quiz_headers/tmnt.jpg',
    },
    {
        'name': 'The Capitals of Asia Quiz',
        'slug': 'capitals-of-asia',
        'description': "I am The Shredder! Wait, I already declared that in my last quiz...\nANYWAY!\nThis quiz will test you on my home continent, Asia, and its capital cities!",
        'pub_date': date(2019, 10, 30),
        'tags': ['asia', 'capitals', 'geography'],
        'author': 'shredder',
        'image': 'quiz_headers/tokyo.jpg'
    },
    {
        'name': 'The Mountains of the World Quiz',
        'slug': 'mountains-of-the-world',
        'description': "Here's a quiz to test your knowledge about the mountains of the world!",
        'pub_date': date(2019, 10, 27),
        'tags': ['geography', 'mountains'],
        'author': 'mojojojo',
        'image': 'quiz_headers/mountains.jpg',
    },
    {
        'name': 'Food From Around The World Quiz',
        'slug': 'food-from-around-the-world',
        'description': "I AM THE SHR...\n\nYou thought I was going to say SHREDDER, didn't you?\n\nHere's a quiz to test your knowledge of the different cuisines of the world!",
        'pub_date': date(2019, 11, 1),
        'tags': ['food'],
        'author': 'shredder',
        'image': 'quiz_headers/food-quiz.jpg',
    },
    {
        'name': 'Video Games Quiz',
        'slug': 'video-games',
        'description': "Mojo Jojo loves playing video games! Now Mojo Jojo will test you!",
        'pub_date': date(2019, 11, 1),
        'tags': ['video-games'],
        'author': 'mojojojo',
        'image': 'quiz_headers/mario.jpeg',
    },
    {
        'name': 'The Omelette du Fromage Quiz',
        'slug': 'omelette-du-fromage',
        'description': "Omelette...",
        'pub_date': date(2019, 11, 4),
        'tags': ['television', 'dexters-lab'],
        'author': 'dexter',
        'image': 'quiz_headers/dexter.jpg',
    },
    {
        'name': 'The "Is Donald Trump an Idiot" Quiz',
        'slug': 'donald-is-an-idiot',
        'description': "The easiest quiz on this website, by far!",
        'pub_date': date(2019, 11, 10),
        'tags': [],
        'author': 'dexter',
        'image': 'quiz_headers/donald-is-an-idiot.jpg',
    },
    {
        'name': 'The Avengers Quiz',
        'slug': 'the-avengers-quiz',
        'description': "You've seen the movies and you've cried at the end of Endgame. But how well do you really know the Avengers?",
        'pub_date': date(2019, 11, 11),
        'tags': ['avengers', 'comics'],
        'author': 'dexter',
        'image': 'quiz_headers/avengers.jpg',
    },
    {
        'name': 'The Book Lovers Quiz',
        'slug': 'the-book-lovers-quiz',
        'description': "I, Shredder, am a bibliophile and an avid reader. As of 2019, I have implemented a strict screening policy to admit only ardent book lovers into my specialized troop of foot soldiers, known as the Novel Ninjas.\nDo you have what it takes to join our ranks? How well do YOU know your books?\n\nP.S: I WILL NOT TOLERATE PAPER SHREDDING JOKES!",
        'pub_date': date(2019, 11, 15),
        'tags': ['books', ],
        'author': 'shredder',
        'image': 'quiz_headers/books.jpg',
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
        if 'image' in quiz_dict:
            quiz.image = quiz_dict['image']
            quiz.max_image_size = max_image_size
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
