import streamlit as st
import pickle
import nltk
import wordcloud
from wordcloud import WordCloud
# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords') 
nltk.download('punkt_tab')

model=pickle.load(open('model.pkl', 'rb'))
tfidf=pickle.load(open('vectorizer.pkl', 'rb'))
# print("Model and vectorizer loaded successfully")

# Text Preprocessing
def text_transform(text):
  import string
  from nltk.corpus import stopwords
  from nltk.stem.porter import PorterStemmer
  ps=PorterStemmer()
  # Lowercase
  text=text.lower()

  # Tokenize
  text=nltk.word_tokenize(text)

  # Removing Special Characters
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)

  # Removing Punctuations and Stopwords
  text=y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  # Stemming- Converting words like dancing/dances/danced to single word dance
  text=y[:]
  y.clear()
  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)



st.title("SMS Spam Classifier")

input_sms = st.text_area("Enter the message")
if st.button('Predict'):
    # 1. Preprocess the input
    transformed_input = text_transform(input_sms)
    
    # 2. Transform the input using the vectorizer
    vector_input = tfidf.transform([transformed_input])
    # 3. Predict using the model
    result = model.predict(vector_input)[0]

    # 4. Display the prediction result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    
