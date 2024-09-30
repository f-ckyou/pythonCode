import random

def text_to_list(file_path):
    with open(file_path, 'r') as file: 
        quiz_list = file.readlines() 

    quiz_list = [trailspace.strip() for trailspace in quiz_list]
    return quiz_list

file_path = 'random-module/hard_high_school_math_quiz.txt'
textlist = text_to_list(file_path)    

def random_questionAnswerPair(textlist):

    random_question = random.choice(range(0,len(textlist), 2))

    question = textlist[random_question]
    correct_answer = textlist[random_question + 1]
    print(question)
    return correct_answer

n = 1
score = 0
while (n <= 5):
    correct_answer = random_questionAnswerPair(textlist)
    user_answer = input("Your answer: ").strip()
    if user_answer.lower() == correct_answer.lower():
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}\n")
    
    n += 1
print(f'\n\nYour score is {score}/5')