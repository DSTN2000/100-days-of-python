from operator import add

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0 
        self.score = 0
        self.question_list = question_list
    def still_has_questions(self):
        try:
            self.question_list[self.question_number]
            return True
        except:
            return False

    def next_question(self):
        
        guess = input(f'Q.{self.question_number+1} {self.question_list[self.question_number].text} (True/False?) ')
        self.check_answer(guess)
        self.question_number += 1

    def check_answer(self, guess, answer=None):
        answer = self.question_list[self.question_number].answer.lower()
        guess = guess.lower()
        if guess == answer:
            print('You got it right!')
            self.score += 1
        else:
            print('That\'s wrong')
        print(f'The correct answer was: {answer}')
        print(f'The current score is: {self.score}/{self.question_number+1} \n')
        
