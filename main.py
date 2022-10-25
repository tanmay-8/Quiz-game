from quiz_brain import QuizBrain
from ui import QuizInterface


quiz = QuizBrain()

ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
