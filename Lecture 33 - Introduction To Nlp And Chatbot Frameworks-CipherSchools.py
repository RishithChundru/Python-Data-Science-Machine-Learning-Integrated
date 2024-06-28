# Tokenization
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text="Natural Language Processing is fascinating."
tokens=word_tokenize(text)
print(tokens)


# Stemming 
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["running","ran","runs"]
stems=[stemmer.stem(word) for word in words]
print(stems)


# Lemmatization
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer=WordNetLemmatizer()
words=["running","ran","runs"]
lemmas=[lemmatizer.lemmatize(word,pos='v') for word in words]
print(lemmas)


# Stop Words
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words=set(stopwords.words('english'))
filtered_text=[words for word in tokens if word.lower() not in stop_words]
print(filtered_text)
