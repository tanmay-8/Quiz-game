import requests
from question_model import Question
import random
import html


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = []
        self.current_question = None
        self.generate()
    
    def generate(self):
        if len(self.question_list)==0:
            api = "https://opentdb.com/api.php?amount=15&type=boolean"
            response = (requests.get(api))
            response.raise_for_status()
            data = response.json()["results"]
            for question in data:
                question_text = html.unescape(question["question"])
                question_answer = html.unescape(question["correct_answer"])
                new_question = Question(question_text, question_answer)
                self.question_list.append(new_question)
        
    def still_has_questions(self):
        return len(self.question_list)!=0

    def next_question(self):
        self.question_number += 1
        self.current_question = random.choice(self.question_list)
        return (f"Q.{self.question_number}: {self.current_question.text} (True/False): ")

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        elif(user_answer=="quit"):
            print(f"Your current score is: {self.score}/{self.question_number}")
            quit()
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
