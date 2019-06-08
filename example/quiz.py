import quiz_list
import random

def get_random_quiz():
    random_quiz_number = random.randint(0, len(quiz_list.quiz_lists) - 1)
    quiz = quiz_list.quiz_lists[random_quiz_number]
    return quiz

def check_answer(quiz_item, answer):
    quiz_answer = quiz_item['answer']
    if answer.find(quiz_answer) != -1:
        return 0
    elif answer == "" or answer.find("다음") != -1:
        return -1
    else:
        return -2

if __name__ == "__main__" :
    pass