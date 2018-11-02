import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('wordnet')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
#from nltk.stem import PorterStemmer

#stemmer = PorterStemmer()

lemmatizer = WordNetLemmatizer()

text = "Hello this is a simple test. This is success"

#Tokenize to sentence
sents = sent_tokenize(text)

#Tokenize to words
words = word_tokenize(text)

#print(nltk.wordpunct_tokenize(sample_sentence))
#Print parts of speech of the tokenized words
'''print(nltk.pos_tag(words))'''

#Tokenizing and Printining Parts of Speech for a real life example
'''
def entities(text):
    return(ne_chunk(
        pos_tag(
            word_tokenize(text))
    ))
tree = entities("“You talk about business, this is the group. And we’re so honoured to have you. And we’re gonna be discussing later on some of the ideas you may have to, as the expression goes, make America great again.”")
tree.pprint()'''

#Lemmatize testing with a sample word
'''
lemma_test_text = "ran"
print(lemmatizer.lemmatize(lemma_test_text, pos="v"))'''

#removing stopwords
sample_sentence = "“You talk about business, this is the group. And we’re so honoured to have you. And we’re gonna be discussing later on some of the ideas you may have to, as the expression goes, make America great again.”"
#conversion to lower case for effective filtering
sample_sentence = sample_sentence.lower()

#using regular expression to filter out punctuation and token the sentence
tokenizer = RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(sample_sentence)

#setting stopwords
stop_words = set(stopwords.words("english"))

#words = stemmer.stem(words)
#lemmatizing and then removing the stopwords
words = [lemmatizer.lemmatize(w) for w in words]
filtered_sample = [w for w in words if not w in stop_words]
print(filtered_sample)
