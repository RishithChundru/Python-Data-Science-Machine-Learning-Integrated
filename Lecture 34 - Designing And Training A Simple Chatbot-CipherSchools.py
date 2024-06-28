# Preprocessing the text data
import pandas as pd
import nltk
# load the dataset
file_path="C:\Summer Training\Dataset.csv"
data=pd.read_csv(file_path)
# Preprocess the data
nltk.download('punkt')
data['Question']=data['Question'].apply(lambda x: ' '.join(nltk.word_tokenize(x.lower())))
print(data.head())



# Vectorizing text data
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(data['Question'])
print(X.shape)



# Training a Text Classification Model
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# split the data into training and test sets
X_train, X_test, y_train, y_test=train_test_split(data['Question'],data['Answer'],test_size=0.2,random_state=42)

# Create a model pipeline
model=make_pipeline(TfidfVectorizer(),MultinomialNB())

# Train the model
model.fit(X_train,y_train)
print("Model training complete.")


# Implementing a function to get chatbot responses

# Function to get a response from the chatbot
def get_response(question):
    question= ' '.join(nltk.word_tokenize(question.lower()))
    answer=model.predict([question])[0]
    return answer

# Testing the function
print(get_response("hi , how are you doing?"))