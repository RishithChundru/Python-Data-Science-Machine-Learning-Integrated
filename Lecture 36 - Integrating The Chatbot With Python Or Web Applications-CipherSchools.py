import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import dash
from dash import dcc,html 
from dash.dependencies import Input,Output
import random

# Load the dataset
file_path="C:\Summer Training\Dataset.csv"
data=pd.read_csv(file_path)

# Preprocess the data
nltk.download('punkt')
data['Question']=data['Question'].apply(lambda x: ' '.join(nltk.word_tokenize(x.lower())))

# split the data into training and test sets
X_train, X_test, y_train, y_test=train_test_split(data['Question'],data['Answer'],test_size=0.2,random_state=42)

# Create a model pipeline
model=make_pipeline(TfidfVectorizer(),MultinomialNB())
model.fit(X_train,y_train)

def get_response(question):
    question= ' '.join(nltk.word_tokenize(question.lower()))
    answer=model.predict([question])[0]
    return answer

# Intialize the dash app
app=dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Chatbot", style={'textAlign': 'center'}),
    dcc.Textarea(
        id='user-input',
        value='Type your Question Here...',
        style={'width': '100%', 'height': 100}
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='chatbot-output', style={'padding': '10px'})
])

# Define callback to update chatbot response
@app.callback(
    Output('chatbot-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('user-input', 'value')]
)
def update_output(n_clicks, user_input):
    if n_clicks > 0:
        response=get_response(user_input)
        return html.Div([
            html.P(f"You: {user_input}", style={'margin': '10px'}),
            html.P(f"Bot: {response}", style={'margin': '10px', 'background-color': '#f0f0f0', 'padding': '10px'})
        ])
    return "Ask me something!"

# Running the app
if __name__ == '__main__':
    app.run_server(debug=True)