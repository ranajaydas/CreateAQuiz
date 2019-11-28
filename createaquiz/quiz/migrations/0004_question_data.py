"""
User created migration file that will initialize the database with
question information, instead of starting with an empty database.
"""
from django.db import migrations

QUESTIONS = [
    {
        'pk': 1,
        'question_text': 'Who is the leader of the Powerpuff Girls?',
        'correct_choice': 'Blossom',
        'incorrect_choice_1': 'Buttercup',
        'incorrect_choice_2': 'Bubbles',
        'incorrect_choice_3': 'Mojo Jojo',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'pk': 2,
        'question_text': 'What colour outfit does Buttercup wear?',
        'correct_choice': 'Green',
        'incorrect_choice_1': 'Pink',
        'incorrect_choice_2': 'Blue',
        'incorrect_choice_3': 'Mojo Jojo!',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'pk': 3,
        'question_text': "What is the colour of Bubble's eyes?",
        'correct_choice': 'Blue',
        'incorrect_choice_1': 'Pink',
        'incorrect_choice_2': 'Green',
        'incorrect_choice_3': 'Death',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'pk': 4,
        'question_text': "Who created the Powerpuff Girls?",
        'correct_choice': 'Professor Utonium',
        'incorrect_choice_1': 'Professor X',
        'incorrect_choice_2': 'Mayor',
        'incorrect_choice_3': 'Mojo Jojo!',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'pk': 5,
        'question_text': "Who is the youngest Powerpuff Girl?",
        'correct_choice': 'Bubbles',
        'incorrect_choice_1': 'Blossom',
        'incorrect_choice_2': 'Buttercup',
        'incorrect_choice_3': 'Mojo Jojo!',
        'quiz_slug': 'know-your-powerpuff-girls',
    },
    {
        'pk': 6,
        'question_text': "Which of these is NOT a Teenage Mutant Ninja Turtle?",
        'correct_choice': 'Caravaggio',
        'incorrect_choice_1': 'Leonardo',
        'incorrect_choice_2': 'Donatello',
        'incorrect_choice_3': 'Michelangelo',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'pk': 7,
        'question_text': "What is Michelangelo's favourite food?",
        'correct_choice': 'Pizza',
        'incorrect_choice_1': 'Burgers',
        'incorrect_choice_2': 'Fish n chips',
        'incorrect_choice_3': 'Weed',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'pk': 8,
        'question_text': "Who is the most handsome enemy of the Teenage Mutant Ninja Turtles?",
        'correct_choice': 'The Shredder',
        'incorrect_choice_1': 'Krang (really?)',
        'incorrect_choice_2': 'Bebop',
        'incorrect_choice_3': 'Rocksteady',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'pk': 9,
        'question_text': "What is the capital of Japan?",
        'correct_choice': 'Tokyo',
        'incorrect_choice_1': 'Kyoto',
        'incorrect_choice_2': 'Osaka',
        'incorrect_choice_3': 'Hiroshima',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'pk': 10,
        'question_text': "What is the capital of India?",
        'correct_choice': 'New Delhi',
        'incorrect_choice_1': 'Calcutta',
        'incorrect_choice_2': 'Mumbai',
        'incorrect_choice_3': 'Bangalore',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'pk': 11,
        'question_text': "What is the capital of Georgia?",
        'correct_choice': 'Tblisi',
        'incorrect_choice_1': 'Nur-Sultan',
        'incorrect_choice_2': 'Bendar Seri Begawan',
        'incorrect_choice_3': 'This is a trick question! Georgia is in Europe!',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'pk': 12,
        'question_text': "Baku is the capital of which country?",
        'correct_choice': 'Azerbaijan',
        'incorrect_choice_1': 'Turkey',
        'incorrect_choice_2': 'Armenia',
        'incorrect_choice_3': 'Turkmenistan',
        'quiz_slug': 'capitals-of-asia',
    },
    {
        'pk': 13,
        'question_text': "What colour mask does Donatello wear?",
        'correct_choice': 'Purple',
        'incorrect_choice_1': 'Red',
        'incorrect_choice_2': 'Blue',
        'incorrect_choice_3': 'Orange',
        'quiz_slug': 'tmnt-quiz',
    },
    {
        'pk': 14,
        'question_text': "Which is the highest peak in the world?",
        'correct_choice': 'Mount Everest',
        'incorrect_choice_1': 'Mount K2',
        'incorrect_choice_2': 'Mount Kanchenjunga',
        'incorrect_choice_3': 'Mount Fuji',
        'quiz_slug': 'mountains-of-the-world',
    },
    {
        'pk': 15,
        'question_text': "Which is the longest mountain range in the world?",
        'correct_choice': 'Andes',
        'incorrect_choice_1': 'Himalayas',
        'incorrect_choice_2': 'Rocky Mountains',
        'incorrect_choice_3': 'Great Dividing Range',
        'quiz_slug': 'mountains-of-the-world',
    },
    {
        'pk': 16,
        'question_text': "Where did sushi originate?",
        'correct_choice': 'Southeast Asia',
        'incorrect_choice_1': 'Japan',
        'incorrect_choice_2': 'China',
        'incorrect_choice_3': 'Korea',
        'quiz_slug': 'food-around-the-world',
    },
    {
        'pk': 17,
        'question_text': "What is the national dish of Bulgaria?",
        'correct_choice': 'Shopska Salad',
        'incorrect_choice_1': 'Lyutenitsa',
        'incorrect_choice_2': 'Ajvar',
        'incorrect_choice_3': 'Tavche Gravche',
        'quiz_slug': 'food-around-the-world',
    },
    {
        'pk': 18,
        'question_text': "What is Pecorino cheese most commonly made from?",
        'correct_choice': 'Sheep milk',
        'incorrect_choice_1': 'Cow milk',
        'incorrect_choice_2': 'Buffalo milk',
        'incorrect_choice_3': 'Turtle milk',
        'quiz_slug': 'food-around-the-world',
    },
    {
        'pk': 19,
        'question_text': "When is Half-Life 3 coming out?",
        'correct_choice': 'Never',
        'incorrect_choice_1': 'Never',
        'incorrect_choice_2': 'Never',
        'incorrect_choice_3': 'Never',
        'quiz_slug': 'video-games',
    },
    {
        'pk': 20,
        'question_text': "What is the french word for omlette with cheese?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Croissant',
        'incorrect_choice_2': 'Je ma pelle le Toots McPoot',
        'incorrect_choice_3': 'Buffet',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'pk': 21,
        'question_text': "What is the most delicious breakfast in the world?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Old shoes',
        'incorrect_choice_2': 'Porridge',
        'incorrect_choice_3': 'Nasi Lemak',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'pk': 22,
        'question_text': "What is the capital of North Korea?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Pyongyang',
        'incorrect_choice_2': 'Seoul',
        'incorrect_choice_3': 'Tokyo',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'pk': 23,
        'question_text': "Who is the president of the US in 2019?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': 'Dubyaman',
        'incorrect_choice_2': 'Arnold Schwarzenegger',
        'incorrect_choice_3': 'Giant wig wearing baby',
        'quiz_slug': 'omelette-du-fromage',
    },
    {
        'pk': 24,
        'question_text': "When is Half-Life 3 coming out?",
        'correct_choice': 'Omelette du fromage',
        'incorrect_choice_1': '2022',
        'incorrect_choice_2': '2122',
        'incorrect_choice_3': '2222',
        'quiz_slug': 'omelette-du-fromage',
    },
]


def add_question_data(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')
    Quiz = apps.get_model('quiz', 'Quiz')
    for question_dict in QUESTIONS:
        question = Question.objects.create(
            pk=question_dict['pk'],
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
        question = Question.objects.get(pk=question_dict['pk'])
        question.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_data'),
    ]

    operations = [
        migrations.RunPython(add_question_data, remove_question_data)
    ]
