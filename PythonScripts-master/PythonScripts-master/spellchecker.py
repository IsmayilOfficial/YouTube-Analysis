import editdistance
import nltk
import numpy as np
from nltk.corpus import brown
from nltk.corpus import stopwords

print "Enter a word"
our_word = raw_input()

all_words = set(brown.words())

if our_word in all_words :
	print "The word you entered is valid."
else :

	# This stop_words list contains all the common stop words in English, like 'a', 'and', 'the' etc. 
	# We remove all those words from the existing set of words
	stop_words = set(stopwords.words('english'))
	filtered_words = [word for word in all_words if not word.lower() in stop_words]
	np_filtered_words = np.array(filtered_words)

	# We find the edit distance between each and every word in the filtered_words_list
	editdistance_array = lambda word: editdistance.eval(our_word, word)
	set_of_editdistance = np.vectorize(editdistance_array)
	edit_distance_for_each_word = set_of_editdistance(np_filtered_words)
	# Here, we find the minimum edit distance, and through numpy, obtain a set which shows 
	# if a particular word has minimum edit distance with our word
	words_with_min_edit_dist = np_filtered_words[ edit_distance_for_each_word == np.amin(edit_distance_for_each_word)]

	print "The word you entered is not valid, try in the list provided."		
	print(words_with_min_edit_dist)
