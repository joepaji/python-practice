#!/usr/bin/env python3
from question_model import Question
from data import generate_question_bank, get_50_questions
from quiz_brain import QuizBrain
from api import get_session_token

session_token = get_session_token()
question_data = get_50_questions(session_token)
question_bank = generate_question_bank(question_data)
quiz = QuizBrain(question_bank)

cont = True
while len(quiz.question_list)>0 and cont:
    answer = quiz.ask_question()
    if answer == 'exit':
        break
    quiz.check_answer(answer)
    if len(quiz.question_list) == 0:
        question_data = get_50_questions(session_token)
        question_bank = generate_question_bank(question_data)
        quiz.question_list = question_bank
quiz.display_game_over()

