from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import pandas as pd

depression_data = pd.read_json('reddit_depression_india_236_posts.json')
suicidewatch_data = pd.read_json('reddit_suicidewatch_india_202_posts.json')

combined_data = pd.concat(
    [depression_data, suicidewatch_data], axis=0, ignore_index=True)

filtered_data = combined_data[["author", "title", "selftext", "is_suicide"]]


def processing_text(series_to_process):
    new_list = []
    tokenizer = RegexpTokenizer(r'(\w+)')
    lemmatizer = WordNetLemmatizer()
    english_stopwords = stopwords.words("english")
    for i in range(len(series_to_process)):
        dirty_string = (series_to_process)[i].lower()
        words_only = tokenizer.tokenize(dirty_string)
        words_only_lem = [lemmatizer.lemmatize(i) for i in words_only]
        words_without_stop = [
            j for j in words_only_lem if j not in english_stopwords]
        long_string_clean = " ".join(word for word in words_without_stop)
        new_list.append(long_string_clean)
    return new_list

filtered_data['title_clean'] = processing_text(filtered_data['title'])
filtered_data['selftext_clean'] = processing_text(filtered_data['selftext'])

filtered_data['megatext_clean'] = filtered_data["title_clean"] + ' ' + filtered_data['selftext_clean']

filtered_data.to_json('cleaned_data.json')