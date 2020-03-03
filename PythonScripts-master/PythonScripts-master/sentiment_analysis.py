# This script accepts a text file and finds out if the text as a whole is positive or negative.
# input python sentiment_analysis.py sample_text.txt

from textblob import TextBlob
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as myfile:
    data=myfile.read()

sentiment_list = []  

blob = TextBlob(data)
for sentence in blob.sentences:
    sentiment_list.append(sentence.sentiment.polarity)

total_sentiment_polarity_value = sum(sentiment_list)

if total_sentiment_polarity_value > 0 :
	print "This sentence is moreorless negative"
elif total_sentiment_polarity_value < 0 :
	print "This sentence is moreorless negative"
else :
	print "This sentence is somewhat neutral"

