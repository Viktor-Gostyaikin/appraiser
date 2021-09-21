import string
from nltk import word_tokenize, Text

# Блок открытия файла


def import_text(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        text = file.read()
    return text

# блок обработки файла


def clean_text(text):
    text_lower = text.lower()
    punctuation_list = string.punctuation + string.digits + '\n\xa0«»\t—…'
    text_without_punctuation = "".join(
        [word for word in text_lower if word not in punctuation_list])
    return(text_without_punctuation)

# Создание списка слов


def token(text):
    text_tokens = word_tokenize(text)
    return text_tokens


def words_count(text):
    return len(text)


def to_text(text):
    return Text(text)


def tf(item: tuple, total_items: int):
    word = item[0]
    count = item[1]
    tf_n = count/total_items
    return [word, tf_n]


def idf(item: list,):
    pass
