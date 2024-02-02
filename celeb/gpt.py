from openai import OpenAI
from .models import *
import json


def questions(keyword):

    client = OpenAI()

    content = 'give me 3, json formatted multiple choice questions with keys {question, options(list with exactly 5 options and no numbers or letters), and answer(the correct option letter)} separated by a comma inside a wrapper json with key questions like, about this topic: ' + f'{
        keyword}'

    # content = '''
    #     Give me a JSON format response about 'Jason Momoa' with keys {name, birth_date, sex, movies_and_shows(at least 5 in the form {name, year, imdb_rating}), and awards(at least 3 with keys {award_name, and year}) } inside of one big wrapper with key {information}.
    # '''

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )
    response = ''
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''

    json_format_questions = dict(json.loads(response))

    print(f'{json_format_questions} \n')

    for question in json_format_questions['questions']:
        print(f'question: {question['question']}')
        print(f'options: {question['options']}')
        print(f'answer: {question['answer']} \n')


def celebDetail(keyword):

    client = OpenAI()

    content = '''
        Give me a JSON format response about ''' + f'{keyword}' + ''' with keys {name (has to be full name if possible), birth_date, sex, movies_and_shows(exactly 5 in the form {title, year, imdb_rating}), and awards(at least 2 at most 3 with keys {award_name, and year}) } inside of one big wrapper with key {information:{}}.
        '''

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        stream=True,
    )
    response = ''
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''

    celeb_details = dict(json.loads(response))
    print(celeb_details)

    return celeb_details
