import quiz
import html
import random

def find_first_letter_of_answer(question):
    '''
    Function that given a question will find out the answer,
    format it then find the first character
    '''
    answer = html.unescape(question['correct_answer'])
    return answer[0]

def find_letters_in_answer(question):
    '''
    Function that given a question will find out the answer,
    format it then find the first character
    '''
    answer = html.unescape(question['correct_answer'])
    return len(answer)

def find_len_nine_answer(num_questions=50, category=None, difficulty=None,
    qtype=None):
    '''
    Function that will generate (potentially) multiple sets of questions
    then loop over them until it finds an answer with 9 characters then
    returns that question
    '''
    # Keep looping until the function returns something
    while True: 
        # Generate a set of questions
        questions = quiz.get_questions_from_json(num_questions, difficulty, category, qtype)
        # Loop through the questions
        for idx in questions:
            # If there are 9 letters in the answer return the questions
            if find_letters_in_answer(idx) == 9 and idx['correct_answer'].find(' ')==-1:
                return idx

def find_answer_with_start_letter(letter, num_questions=50, category=None, difficulty=None,
    qtype=None):
    '''
    Function that will generate (potentially) multiple sets of questions
    then loop over them until it finds an answer that starts with a particular letter
    '''
    # Keep looping until the function returns something
    while True:
        # Generate a set of questions
        questions = quiz.get_questions_from_json(num_questions, difficulty, category, qtype)
        # Loop through the questions
        for idx in questions:
            # If the first letter matches return that answer
            if find_first_letter_of_answer(idx) == letter.upper():
                return idx

print(find_answer_with_start_letter('o'))

def find_answers_matching_anagram(anagram_question,category=None, difficulty=None,
    qtype=None):
    '''
    Function that given a question finds the correct answer then loops through
    it appending a question for each letter in the answer
    '''
    questions = []
    # Loops through the letters in the answer
    for idx in anagram_question['correct_answer']:
        # Appends an question for each letter
        questions.append(find_answer_with_start_letter(idx, category=category, difficulty=difficulty,
                                                        qtype=qtype))
    return questions
        
def get_anagram_and_questions(category=None, difficulty=None, qtype=None):
    '''
    Function to get a question that is of length 9 then find letter
    link questions for it, then shuffle those questions.
    '''
    anagram_question = find_len_nine_answer(category=category, difficulty=difficulty,
                                            qtype=qtype)
    questions = find_answers_matching_anagram(anagram_question)
    questions = quiz.randomly_order_list(questions)
    return questions + [anagram_question]

quiz.display_results(get_anagram_and_questions(category=9))