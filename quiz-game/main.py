from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.question_there_or_not():
    quiz.question()
print("You've just completed the Quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
os.system("pause")
