# From the dataset obtained from Kaggle which has data comments obtained on youtube videos.
# Source of dataset = https://www.kaggle.com/datasets
import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

comments_with_likes = []
comments_without_likes = []

with open('UScomments.csv', 'rb') as csvfile:

	# This csv file had some "NULL" values, so we're removing all such values 

	reader = csv.reader(x.replace('\0', '') for x in csvfile)
	for row in reader:
		# The 3rd and 4th column contains likes and unlikes. Those are taken in as integers
		if row[2].isdigit() :
			row[2] = int(row[2])
		if row[3].isdigit() :	 
			row[3] = int(row[3])
		# We make sure that we only take the comments which has some likes	
		if row[2] > 0 :
			comments_with_likes.append(row[1])
		else :
			comments_without_likes.append(row[1])



data = comments_with_likes + comments_without_likes
target = len(comments_with_likes) * [0] 
target = target + len(comments_without_likes) * [1]
category_values = ["like", "unlike"]
train = {}
train["data"] = data
train["target"] = np.array(target)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train["data"])

tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

docs_new = ['Text to be added']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)


clf = MultinomialNB().fit(X_train_tfidf, train["target"])
predicted = clf.predict(X_new_tfidf)
for doc, category in zip(docs_new, predicted): 
	print('%r => %s' % (doc, category_values[category]))





    


