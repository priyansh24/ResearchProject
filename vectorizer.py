from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import HashingVectorizer
import pandas as pd

tfidf_vec = TfidfVectorizer()
count_vec = CountVectorizer()
# hashing_vec = HashingVectorizer()

doc_list = [
    "Deepam deepam deepam deepam loves python",
    "Deepam hates Java",
    "Bhoomika is awesome",
    "Madhumita is a good coder."
]

data = pd.read_json("reddit_depression_india_236_posts.json")
doc_list = data['selftext'].tolist()
# print(data['selftext'].tolist())


def get_term_dataframe(doc_list, vectorizer):
    term_matrix = vectorizer.fit_transform(doc_list)
    return pd.DataFrame(term_matrix.toarray(), columns=vectorizer.get_feature_names())


# print('Count result')
# print(get_term_dataframe(doc_list, count_vec))
print('\nTFIDF result')
term_df = get_term_dataframe(doc_list, tfidf_vec)
# print(term_df)
print(term_df.columns.tolist())

# cosine similarity