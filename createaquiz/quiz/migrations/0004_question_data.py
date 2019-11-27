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
