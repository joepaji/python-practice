import random
class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Gets the next question from the question bank."""
        question = random.choice(self.question_list)
        self.question_list.remove(question)
        self.question_number += 1
        return question

    def ask_question(self):
        """Ask a new question. Returns the users answer."""
        question = self.next_question()
        self.question = question
        answer = '_!'
        if answer != 't' and answer != 'f' and answer != 'exit':
            while answer != 't' and answer != 'f' and answer != 'exit':
                if answer != '_!': 
                    print("Invalid input. Try again.")
                answer = input(f"Q.{self.question_number}: {question.question} True or False? (T/F): ").lower()
        if answer == 't':
            answer = "True"
        elif answer == 'f':
            answer = "False"
        
        return answer
    
    def check_answer(self, answer):
        """Check if answer is correct and handle score."""
        if answer == self.question.answer:
            self.score += 1
            print(f"You are correct! Score: {self.score}/{self.question_number}")
        else:
            print(f"That's incorrect. Score: {self.score}/{self.question_number}")

    def display_game_over(self):
        print(f"Game over! Final Score: {self.score}/{self.question_number}")