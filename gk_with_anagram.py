import quiz
import html
import random

def find_first_letter_of_answer(question):
    answer = html.unescape(question['correct_answer'])
    return answer[0]

def find_letters_in_answer(question):
    answer = html.unescape(question['correct_answer'])
    return len(answer)

def find_len_nine_answer(num_questions=50, category=None, difficulty=None,
    qtype=None):
    while True:
        questions = quiz.get_questions_from_json(num_questions, difficulty, category, qtype)
        for idx in questions:
            if find_letters_in_answer(idx) == 9 and idx['correct_answer'].find(' ')==-1:
                return idx

def find_answer_with_start_letter(letter,
    num_questions=50, category=None, difficulty=None,
    qtype=None):
    while True:
        questions = quiz.get_questions_from_json(num_questions, difficulty, category, qtype)
        for idx in questions:
            if find_first_letter_of_answer(idx) == letter.upper():
                return idx

print(find_answer_with_start_letter('o'))

def find_answers_matching_anagram(anagram_question,category=None, difficulty=None,
    qtype=None):
    questions = []
    for idx in anagram_question['correct_answer']:
        questions.append(find_answer_with_start_letter(idx, category=category, difficulty=difficulty,
                                                        qtype=qtype))
    return questions
        
def get_anagram_and_questions(category=None, difficulty=None,
    qtype=None):
    anagram_question = find_len_nine_answer(category=category, difficulty=difficulty,
                                            qtype=qtype)
    questions = find_answers_matching_anagram(anagram_question)
    questions = quiz.randomly_order_list(questions)
    return questions + [anagram_question]

quiz.display_results(get_anagram_and_questions(category=9, qtype='booleon'))