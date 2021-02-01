"""Research @ IET.ipynb

Original file is located at
    https://colab.research.google.com/drive/1OhSOnmqUxkLLY9YsBXuqx-yZ6Syuy4jN

# Test cases
1. w/ stopwords and w/o stopwords
1. textblob v/s vader
1. sentences segregation
"""

# importing important libraries

import json

import numpy as np

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from textblob import TextBlob

from dictionary import custom_dictionary

import matplotlib.pyplot as plt


def remove_stopwords_from_para(para: str) -> str:
    stopwords_list = stopwords.words('english')
    stopwords_tagged = nltk.tag.pos_tag(stopwords_list)
    stopwords_wo_pronoun = [
        word[0] for word in stopwords_tagged if word[1] not in ['PRP', 'PRP$']][1:]

    final_para_list = []
    for word in word_tokenize(para):
        if word not in stopwords_wo_pronoun:
            final_para_list.append(word)

    return " ".join(final_para_list)


def get_sentences_from_para(para: str) -> list:
    return sent_tokenize(para)


def segregate_sentences_class_wise(sent_list: list, dictionary: dict) -> dict:
    # filtering the sentences according to categories
    sentences_class_wise = {key: [] for key in dictionary.keys()}
    for sent in sent_list:
        for tag in dictionary:
            if set(word_tokenize(sent)).intersection(dictionary[tag]):
                sentences_class_wise[tag].append(sent)
    return sentences_class_wise


# using TextBlob
def get_sentiments_class_wise_texblob(sentences_class_wise: dict, dictionary: dict) -> dict:
    sentiment_class_wise = {}
    for tag in dictionary:
        score = [
            TextBlob(sent).sentiment.polarity for sent in sentences_class_wise[tag]]
        sentiment_class_wise[tag] = np.mean(score) if score else 0
    return sentiment_class_wise


# using vader
def get_sentiments_class_wise_vader(sentences_class_wise: dict, dictionary: dict) -> dict:
    sid = SentimentIntensityAnalyzer()
    sentiment_class_wise = {}
    for tag in dictionary:
        score = [sid.polarity_scores(sent)["compound"]
                 for sent in sentences_class_wise[tag]]
        sentiment_class_wise[tag] = np.mean(score) if score else 0
    return sentiment_class_wise


def process_post(post: str) -> dict:
    return get_sentiments_class_wise_vader(
        segregate_sentences_class_wise(
            get_sentences_from_para(
                remove_stopwords_from_para(post)),
            custom_dictionary),
        custom_dictionary)


def process_all_posts(all_posts: list) -> list:
    all_sentiment_list = []

    for i, post in enumerate(all_posts):
        all_sentiment_list.append(process_post(post['selftext']))
        print(f'post {i} done...')

    return all_sentiment_list


def save_to_file(output_file_path: str, lst: list) -> None:
    f = open(output_file_path, 'w')
    f.write(json.dumps(lst, ensure_ascii=False))
    f.close()


def plot_score(sentiment_scores: dict) -> None:
    score_for_one = process_post(sentiment_scores)

    class_list = list(score_for_one.keys())
    value_list = list(score_for_one.values())

    plt.xlabel('Classes')
    plt.ylabel('Scores')
    plt.title('Class-wise sentiment score for one post')

    plt.bar(class_list, value_list)
    plt.axhline(y=0, color='k', lw=0.5)

    plt.show()
