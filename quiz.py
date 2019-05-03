import requests
import urllib
import html
import random

def create_url(num_questions=10, difficulty=None, category=None, qtype=None):
    '''
    Difficulty: string - value of easy, medium, hard
    Type: string - value of multiple, booleon
    Categories: integer - See categories dictionary
    Num Questions: integer - <50
    '''
    url = 'https://opentdb.com/api.php?amount=' + str(num_questions)
    if category:
        url += '&category=' + str(category)
    if difficulty:
        url += '&difficulty=' + str(difficulty)
    if difficulty:
        url += '&type=' + str(qtype)
    return url

categories = {'General Knowledge': 9, 'Entertainment: Books': 10, 'Enterainment: Films': 11,
		'Entertainment: Music': 12, 'Entertainment: Musicals & Theatre': 13,
		'Entertainment: Television': 14, 'Entertainment: Video Games': 15,
		'Entertainment: Board Games': 16, 'Science & Nature': 17, 'Science: Computers': 18,
		'Science: Mathematics': 19, 'Mythology': 20, 'Sports': 21, 'Geography': 22,
		'History': 23, 'Politics': 24, 'Art': 25, 'Celebrities': 26, 'Animals': 27,
		'Vehicles': 28, 'Entertainment: Comics':29, 'Science: Gadgets': 30,
		'Entertainment: Japanese Anime & Manga': 31, 'Entertainment: Cartoons & Animation': 32}

def get_questions_from_json(num_questions=10, difficulty=None, category=None, qtype=None):
    response = requests.get(create_url(num_questions, difficulty, category, qtype))
    response = response.json()
    return response['results']

def randomly_order_list(list_of_answers):
    random.shuffle(list_of_answers)
    return html.unescape(list_of_answers)

def remove_crap_out_of_answers(list_of_answers):
    clean_list = []
    for idx in list_of_answers:
        clean_list.append(html.unescape(idx))
    return clean_list

def reformat_answers_list(correct_answer, incorrect_answer):
    randomly_ordered_answers = randomly_order_list([correct_answer] + incorrect_answer)
    return remove_crap_out_of_answers(randomly_ordered_answers)

def display_results(questions_to_be_displayed):
    for counter, idx in enumerate(questions_to_be_displayed):
        print('Question:', counter+1)
        print(html.unescape(idx['question']))
        answers = reformat_answers_list(idx['correct_answer'], idx['incorrect_answers'])
        print('Possible Answers: ' + ", ".join(answers))
        print('Answer:', idx['correct_answer'].replace('&quot:', ''))
        print('')

response = get_questions_from_json(num_questions=20, category=18)
display_results(response)