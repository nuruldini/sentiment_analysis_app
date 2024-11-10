import streamlit as st
from transformers import pipeline
import pandas as pd
import io

# Title of the app
st.title("Sentiment Analysis App")

# Load pre-trained sentiment analysis model from Hugging Face
sentiment_analyzer = pipeline('sentiment-analysis')

# User input: Sentence or File upload
input_type = st.selectbox("Select input type", ("Sentence", "File"))

# Sentiment analysis for a sentence
if input_type == "Sentence":
    sentence = st.text_input("Enter a sentence:")
    if sentence:
        # Sentiment analysis using Hugging Face's transformer model
        result = sentiment_analyzer(sentence)
        sentiment = result[0]['label']
        if sentiment == "POSITIVE":
            st.write("Sentiment: Positive")
        elif sentiment == "NEGATIVE":
            st.write("Sentiment: Negative")
        else:
            st.write("Sentiment: Neutral")

# Sentiment analysis for a file upload
elif input_type == "File":
    uploaded_file = st.file_uploader("Upload a text file", type=["txt", "csv"])
    if uploaded_file is not None:
        # Read and process the uploaded file
        if uploaded_file.name.endswith('csv'):
            df = pd.read_csv(uploaded_file)
            # Assuming there's a column with text data, modify if needed
            for index, row in df.iterrows():
                text = row[0]  # assuming text is in the first column
                result = sentiment_analyzer(str(text))
                sentiment = result[0]['label']
                st.write(f"Sentence: {text}")
                if sentiment == "POSITIVE":
                    st.write("Sentiment: Positive")
                elif sentiment == "NEGATIVE":
                    st.write("Sentiment: Negative")
                else:
                    st.write("Sentiment: Neutral")
        elif uploaded_file.name.endswith('txt'):
            file_content = uploaded_file.read().decode("utf-8")
            sentences = file_content.splitlines()
            for sentence in sentences:
                result = sentiment_analyzer(sentence)
                sentiment = result[0]['label']
                st.write(f"Sentence: {sentence}")
                if sentiment == "POSITIVE":
                    st.write("Sentiment: Positive")
                elif sentiment == "NEGATIVE":
                    st.write("Sentiment: Negative")
                else:
                    st.write("Sentiment: Neutral")
