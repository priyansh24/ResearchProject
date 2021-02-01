import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_json('cleaned_data.json')

X = data["megatext_clean"]
y = data["is_suicide"]

max_features=50

# 60 40
# 70 30
# 80 20
# visualization
# KNN
# ye use kiya to kyu use kiya???
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

tvec_optimised = TfidfVectorizer(
    max_df=0.5, max_features=max_features, min_df=2, ngram_range=(1, 3), stop_words='english')
X_train_tvec = tvec_optimised.fit_transform(X_train).todense()
X_test_tvec = tvec_optimised.transform(X_test).todense()

hvec_optimised = HashingVectorizer(
    n_features=max_features, stop_words='english', alternate_sign=False)
X_train_hvec = hvec_optimised.fit_transform(X_train).todense()
X_test_hvec = hvec_optimised.transform(X_test).todense()

# MultinomialNB
mnb = MultinomialNB()
mnb.fit(X_train_tvec, y_train)
taccuracy = mnb.score(X_test_tvec, y_test)


# print(X_train_tvec)
# print(X_train_hvec)

rfc = RandomForestClassifier(random_state=10)
rfc.fit(X_train_hvec, y_train)
haccuracy = rfc.score(X_test_hvec, y_test)

trfc = RandomForestClassifier(random_state=10)
trfc.fit(X_train_tvec, y_train)
trfcaccuracy = rfc.score(X_test_tvec, y_test)

hmnb = MultinomialNB()
hmnb.fit(X_train_tvec, y_train)
hmnbaccuracy = hmnb.score(X_test_tvec, y_test)

print(f"TfidfVectorizer + MultinomialNB : {taccuracy * 100}")
print(f"HashingVectorizer + RandomForestClassifier : {haccuracy * 100}")
print(f"TfidfVectorizer + RandomForestClassifier : {trfcaccuracy * 100}")
print(f"HashingVectorizer + MultinomialNB : {hmnbaccuracy * 100}")