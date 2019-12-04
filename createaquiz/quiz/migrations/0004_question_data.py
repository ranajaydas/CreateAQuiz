"""
User created migration file that will initialize the database with
question information, instead of starting with an empty database.
"""
from django.db import migrations

QUESTIONS = [
    {
        'question_text': 'Who is the leader of the Powerpuff Girls?',
        'correct_choice': 'Blossom',
        'incorrect_choice_1': 'Buttercup',
        'incorrect_choice_2': 'Bubbles',
        'incorrect_choice_3': 'Mojo Jojo',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'question_text': 'What colour outfit does Buttercup wear?',
        'correct_choice': 'Green',
        'incorrect_choice_1': 'Pink',
        'incorrect_choice_2': 'Blue',
        'incorrect_choice_3': 'Mojo Jojo!',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'question_text': "What is the colour of Bubble's eyes?",
        'correct_choice': 'Blue',
        'incorrect_choice_1': 'Pink',
        'incorrect_choice_2': 'Green',
        'incorrect_choice_3': 'Death',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'question_text': "Who created the Powerpuff Girls?",
        'correct_choice': 'Professor Utonium',
        'incorrect_choice_1': 'Professor X',
        'incorrect_choice_2': 'Mayor',
        'incorrect_choice_3': 'Mojo Jojo!',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'question_text': "Who is the youngest Powerpuff Girl?",
        'correct_choice': 'Bubbles',
        'incorrect_choice_1': 'Blossom',
        'incorrect_choice_2': 'Buttercup',
        'incorrect_choice_3': 'Mojo Jojo!',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'question_text': "Which of these is NOT a Teenage Mutant Ninja Turtle?",
        'correct_choice': 'Caravaggio',
        'incorrect_choice_1': 'Leonardo',
        'incorrect_choice_2': 'Donatello',
        'incorrect_choice_3': 'Michelangelo',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'question_text': "What is Michelangelo's favourite food?",
        'correct_choice': 'Pizza',
        'incorrect_choice_1': 'Burgers',
        'incorrect_choice_2': 'Fish n chips',
        'incorrect_choice_3': 'Weed',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'question_text': "Who is the most handsome enemy of the Teenage Mutant Ninja Turtles?",
        'correct_choice': 'The Shredder',
        'incorrect_choice_1': 'Krang (really?)',
        'incorrect_choice_2': 'Bebop',
        'incorrect_choice_3': 'Rocksteady',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'question_text': "What colour mask does Donatello wear?",
        'correct_choice': 'Purple',
        'incorrect_choice_1': 'Red',
        'incorrect_choice_2': 'Blue',
        'incorrect_choice_3': 'Orange',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'question_text': "What is the capital of Japan?",
        'correct_choice': 'Tokyo',
        'incorrect_choice_1': 'Kyoto',
        'incorrect_choice_2': 'Osaka',
        'incorrect_choice_3': 'Hiroshima',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'question_text': "What is the capital of India?",
        'correct_choice': 'New Delhi',
        'incorrect_choice_1': 'Calcutta',
        'incorrect_choice_2': 'Mumbai',
        'incorrect_choice_3': 'Bangalore',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'question_text': "What is the capital of Georgia?",
        'correct_choice': 'Tblisi',
        'incorrect_choice_1': 'Nur-Sultan',
        'incorrect_choice_2': 'Bendar Seri Begawan',
        'incorrect_choice_3': 'This is a trick question! Georgia is in Europe!',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'question_text': "Baku is the capital of which country?",
        'correct_choice': 'Azerbaijan',
        'incorrect_choice_1': 'Turkey',
        'incorrect_choice_2': 'Armenia',
        'incorrect_choice_3': 'Turkmenistan',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'question_text': "Which is the highest peak in the world?",
        'correct_choice': 'Mount Everest',
        'incorrect_choice_1': 'Mount K2',
        'incorrect_choice_2': 'Mount Kanchenjunga',
        'incorrect_choice_3': 'Mount Fuji',
        'quiz_slug': 'mountains-of-the-world',
    },
    {
        'question_text': "Which is the longest mountain range in the world?",
        'correct_choice': 'Andes',
        'incorrect_choice_1': 'Himalayas',
        'incorrect_choice_2': 'Rocky Mountains',
        'incorrect_choice_3': 'Great Dividing Range',
        'quiz_slug': 'mountains-of-the-world',
    },
    {
        'question_text': "Where did sushi originate?",
        'correct_choice': 'Southeast Asia',
        'incorrect_choice_1': 'Japan',
        'incorrect_choice_2': 'China',
        'incorrect_choice_3': 'Korea',
        'quiz_slug': 'food-from-around-the-world',
    },
    {
        'question_text': "What is the national dish of Bulgaria?",
        'correct_choice': 'Shopska Salad',
        'incorrect_choice_1': 'Lyutenitsa',
        'incorrect_choice_2': 'Ajvar',
        'incorrect_choice_3': 'Tavche Gravche',
        'quiz_slug': 'food-from-around-the-world',
    },
    {
        'question_text': "What is Pecorino cheese most commonly made from?",
        'correct_choice': 'Sheep milk',
        'incorrect_choice_1': 'Cow milk',
        'incorrect_choice_2': 'Buffalo milk',
        'incorrect_choice_3': 'Turtle milk',
        'quiz_slug': 'food-from-around-the-world',
    },
    {
        'question_text': "When is Half-Life 3 coming out?",
        'correct_choice': 'Never',
        'incorrect_choice_1': 'Never',
        'incorrect_choice_2': 'Never',
        'incorrect_choice_3': 'Never',
        'quiz_slug': 'video-games',
    },
    {
        'question_text': "What is the name of Mario's brother?",
        'correct_choice': 'Luigi',
        'incorrect_choice_1': 'Green Mario',
        'incorrect_choice_2': 'Mario has no brother!',
        'incorrect_choice_3': 'Mushroom-top',
        'quiz_slug': 'video-games',
    },
    {
        'question_text': "Which was the first video game ever made?",
        'correct_choice': 'Pong',
        'incorrect_choice_1': 'Pacman',
        'incorrect_choice_2': 'Space Invaders',
        'incorrect_choice_3': 'Doom',
        'quiz_slug': 'video-games',
    },
    {
        'question_text': "Which was Studio CD Projekt Red's first game?",
        'correct_choice': 'The Witcher',
        'incorrect_choice_1': 'Cyberpunk 2077',
        'incorrect_choice_2': 'Bastion',
        'incorrect_choice_3': 'Transistor',
        'quiz_slug': 'video-games',
    },
    {
        'question_text': "What is the french word for omlette with cheese?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Croissant',
        'incorrect_choice_2': 'Je ma pelle le Toots McPoot',
        'incorrect_choice_3': 'Buffet',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'question_text': "What is the most delicious breakfast in the world?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Old shoes',
        'incorrect_choice_2': 'Porridge',
        'incorrect_choice_3': 'Nasi Lemak',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'question_text': "What is the capital of North Korea?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Pyongyang',
        'incorrect_choice_2': 'Seoul',
        'incorrect_choice_3': 'Tokyo',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'question_text': "Who is the president of the US in 2019?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Dubyaman',
        'incorrect_choice_2': 'Arnold Schwarzenegger',
        'incorrect_choice_3': 'Giant wig wearing baby',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'question_text': "When is Half-Life 3 coming out?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': '2022',
        'incorrect_choice_2': '2122',
        'incorrect_choice_3': '2222',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'question_text': "Is Donald Trump an idiot?",
        'correct_choice': 'Do you even need to ask? Yes!',
        'incorrect_choice_1': 'No',
        'incorrect_choice_2': 'Maybe',
        'incorrect_choice_3': "He's a genius!",
        'quiz_slug': 'donald-is-an-idiot',
    },
    {
        'question_text': "What is Thor's full name?",
        'correct_choice': 'Thor Odinson',
        'incorrect_choice_1': 'Thor Colson',
        'incorrect_choice_2': 'Thor Nordson',
        'incorrect_choice_3': 'Robert Paulson',
        'quiz_slug': 'the-avengers-quiz',
    },
    {
        'question_text': "Who is Steve Rogers better known as?",
        'correct_choice': 'Captain America',
        'incorrect_choice_1': 'Ironman',
        'incorrect_choice_2': 'The Incredible Hulk',
        'incorrect_choice_3': 'Ant Man',
        'quiz_slug': 'the-avengers-quiz',
    },
    {
        'question_text': "Who was Ant Man after Hank Pym?",
        'correct_choice': 'Scott Lang',
        'incorrect_choice_1': 'Pepper Pym',
        'incorrect_choice_2': 'Tony Stark',
        'incorrect_choice_3': 'Darren Cross',
        'quiz_slug': 'the-avengers-quiz',
    },
    {
        'question_text': "Who is Star Lord's father?",
        'correct_choice': 'Ego',
        'incorrect_choice_1': 'Xenu',
        'incorrect_choice_2': 'Who??',
        'incorrect_choice_3': 'Thor',
        'quiz_slug': 'the-avengers-quiz',
    },
    {
        'question_text': "Who was the first actor to play the Incredible Hulk?",
        'correct_choice': 'Lou Ferrigno',
        'incorrect_choice_1': 'Edward Norton',
        'incorrect_choice_2': 'Eric Bana',
        'incorrect_choice_3': 'Mark Ruffalo',
        'quiz_slug': 'the-avengers-quiz',
    },
    {
        'question_text': "What is the name of Thor's hammer?",
        'correct_choice': 'Mjolnir',
        'incorrect_choice_1': 'Megingjord',
        'incorrect_choice_2': 'Uru',
        'incorrect_choice_3': 'Jarnbjorn',
        'quiz_slug': 'the-avengers-quiz',
    },
    {
        'question_text': "Who wrote the book- The Catcher in the Rye?",
        'correct_choice': 'J.D. Salinger',
        'incorrect_choice_1': 'James Joyce',
        'incorrect_choice_2': 'Ernest Hemingway',
        'incorrect_choice_3': 'George Orwell',
        'quiz_slug': 'the-book-lovers-quiz',
    },
    {
        'question_text': "The movie, Apocalypse Now, is based on which book?",
        'correct_choice': 'Heart of Darkness',
        'incorrect_choice_1': '1984',
        'incorrect_choice_2': 'Lord of the Flies',
        'incorrect_choice_3': 'A Farewell to Arms',
        'quiz_slug': 'the-book-lovers-quiz',
    },
    {
        'question_text': "Which of these was NOT written by James Joyce?",
        'correct_choice': 'The Picture of Dorian Gray',
        'incorrect_choice_1': 'Ulysses',
        'incorrect_choice_2': 'A Portrait of the Artist as a Young Man',
        'incorrect_choice_3': 'Dubliners',
        'quiz_slug': 'the-book-lovers-quiz',
    },
    {
        'question_text': "Which is the only book written by Emily Brontë?",
        'correct_choice': 'Wuthering Heights',
        'incorrect_choice_1': 'Pride and Prejudice',
        'incorrect_choice_2': 'To Kill a Mockingbird',
        'incorrect_choice_3': 'Jane Eyre',
        'quiz_slug': 'the-book-lovers-quiz',
    },
    {
        'question_text': "Which of these books is considered to be one of the first written novels in the world?",
        'correct_choice': 'The Tale of Genji by Murasaki Shikibu',
        'incorrect_choice_1': 'The Gutenberg Bible',
        'incorrect_choice_2': "Le Morte d'Arthur by Thomas Malory",
        'incorrect_choice_3': "Gulliver's Travels by Jonathan Swift",
        'quiz_slug': 'the-book-lovers-quiz',
    },
    {
        'question_text': "Which of these authors is still alive (as of 2019)?",
        'correct_choice': 'Margaret Atwood',
        'incorrect_choice_1': 'Gabriel García Márquez',
        'incorrect_choice_2': "Jane Austen",
        'incorrect_choice_3': "Ayn Rand",
        'quiz_slug': 'the-book-lovers-quiz',
    },
    {
        'question_text': "Which of these famous authors had a Fatwa issued on their life and had to go into hiding?",
        'correct_choice': 'Salman Rushdie',
        'incorrect_choice_1': 'Arundhati Roy',
        'incorrect_choice_2': "Marquis de Sade",
        'incorrect_choice_3': "Vikram Seth",
        'quiz_slug': 'the-book-lovers-quiz',
    },
]


def add_question_data(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    Quiz = apps.get_model('quiz', 'Quiz')
    for question_dict in QUESTIONS:
        question = Question.objects.create(
            question_text=question_dict['question_text'],
            correct_choice=question_dict['correct_choice'],
            incorrect_choice_1=question_dict['incorrect_choice_1'],
            incorrect_choice_2=question_dict['incorrect_choice_2'],
            incorrect_choice_3=question_dict['incorrect_choice_3'],
            quiz=Quiz.objects.get(slug=question_dict['quiz_slug']),
        )
        question.save()


def remove_question_data(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    for question_dict in QUESTIONS:
        question = Question.objects.get(question_text=question_dict['question_text'],
                                        quiz__slug=question_dict['quiz_slug'])
        question.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_data'),
    ]

    operations = [
        migrations.RunPython(add_question_data, remove_question_data)
    ]
