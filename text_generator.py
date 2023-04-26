import nltk
from collections import Counter
import random

corpus = input()

with open(f'{corpus}', 'r', encoding='utf-8') as file:
    text = file.read()
    tokenized = list(nltk.bigrams(text.split()))


counter = 0

while counter != 10:
    word = random.choice(text.split())
    while word != word.capitalize() or '.' in word or '!' in word \
            or '?' in word:
        word = random.choice(text.split())
    sentence = [word]
    # if not sentence:
    #     word = word.capitalize()
    # sentence.append(word)
    for x in range(len(text)):
        words_list = []
        word = sentence[x]

        for y in tokenized:
            if y[0] == word:
                words_list.append(y[1])
        words_counter = Counter(words_list).most_common()

        chances = []
        words = []

        for pair in words_counter:
            chances.append(pair[1])
            words.append(pair[0])

        if x < 4:
            sentence.append(*random.choices(words, chances))
        else:
            if '.' in sentence[-1] or '!' in sentence[-1] or '?' in sentence[-1]:
                break
            else:
                sentence.append(*random.choices(words, chances))

    print(" ".join(sentence))
    counter += 1
