from question_model import *
from data import *
from quiz_brain import *

question_bank = [QuizQuestion(question['text'], question['answer']) for question in question_data]

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f'You\'ve completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}')