# 154
from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    q_text = q["text"]
    q_answer = q["answer"]
    question_bank.append(Question(q_text, q_answer))


# print(len(question_bank))
