import random

def shuffle_words(list_of_words):
    shuffled_words = []
    for idx in list_of_words:
        l = list(idx)
        random.shuffle(l)
        result = ''.join(l)
        shuffled_words.append(result)
    return shuffled_words

words = ['christianity', 'goodfriday', 'crucifixion', 'resurrection', 'bunnyrabbit',
        'easteregghunt', 'chocolate', 'easterservice', 'bouquet', 'vacation']
print(shuffle_words(words))