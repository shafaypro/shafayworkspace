from nltk import sent_tokenize, \
	word_tokenize  # these both are for the tokenizing purposes such that the code tokenize the respectable input using these modules.

# nltk.download()  # autodownloader for the nlp pacakage!
example_text = "Hello there Mr. Smith, Hi my name is muhammad Shafay Amjad, How are you today ? The weather is great and python is awesome.The sky is Blue"
print (sent_tokenize(example_text))  # sentence token woization
tokenized_words = word_tokenize(example_text)  # this is for the word tokenization
for word in tokenized_words:  # this loops through all the words list and then print the word item by item.
	print (word)
