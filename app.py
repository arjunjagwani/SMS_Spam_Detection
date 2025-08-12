import streamlit as st
import pickle

model=pickle.load(open('model.pkl', 'rb'))
tfidf=pickle.load(open('vectorizer.pkl', 'rb'))
print("Model and vectorizer loaded successfully")
