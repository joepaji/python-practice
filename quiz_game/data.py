import api
import requests
from question_model import Question

def get_50_questions(session_token):
    """Gets list of 50 questions from OpenTrivia database."""
    url = api.get_api_url()
    url += f'&{session_token}'
    question_data = []

    response = requests.get(url)

    if response is not None and response.ok:
        data = response.json()

    data_list = data['results']

    for item in data_list:
        question = item['question']
        question = question.replace('&#039','\'')
        question = question.replace('&quot;', '\"')
        question = question.replace('\\\'', '\'')
        question = question.replace(';', '')
        answer = item['correct_answer']
        question_data.append({'text': question, 'answer': answer})

    return question_data

def generate_question_bank(question_data):
    """Generates question bank of Question objects from list of question dictionaries in string format."""
    question_bank = []
    for item in question_data:
        question = Question(item["text"], item["answer"])
        question_bank.append(question)

    return question_bank