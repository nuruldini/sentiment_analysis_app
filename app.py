import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="🌟",
    layout="centered"
)

st.title("🌟 Sentiment Analysis App 🌟")
st.write("""
Welcome to the **Sentiment Analysis App**!  
Type a sentence below to analyze its sentiment as **Positive**, **Negative**, or **Neutral**.
""")

st.sidebar.title("About")
st.sidebar.info("""
This app uses the **VADER Sentiment Analysis** model to evaluate the sentiment of user-provided text.  
Created with ❤️ using [Streamlit](https://streamlit.io).
""")

st.subheader("Enter a sentence:")
sentence = st.text_input("Type your sentence below:")

if sentence:
    # Use VADER to compute sentiment scores
    scores = sia.polarity_scores(sentence)
    compound_score = scores['compound']

    if compound_score >= 0.05:
        sentiment = "Positive 😊"
    elif compound_score <= -0.05:
        sentiment = "Negative 😔"
    else:
        sentiment = "Neutral 😐"

    st.write("### Sentiment Analysis Result:")
    st.markdown(f"**Sentiment:** {sentiment}")
    # Removed detailed scores from output

st.markdown("---")
st.markdown("""
<style>
footer {visibility: hidden;}
.reportview-container .main footer {visibility: hidden;}
header {visibility: hidden;}
</style>
<div style="text-align: center; color: gray;">
    <small>Developed with ❤️ by NURUL DINI FAQRIAH</small>
</div>
""", unsafe_allow_html=True)
