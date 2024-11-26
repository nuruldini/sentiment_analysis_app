import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon if not already available
nltk.download("vader_lexicon")

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="🌟",
    layout="centered"
)

# Page title and description
st.title("🌟 Sentiment Analysis App 🌟")
st.write("""
Welcome to the **Sentiment Analysis App**!  
Type a sentence below to analyze its sentiment as **Positive**, **Negative**, or **Neutral**.
""")

# Sidebar styling and information
st.sidebar.title("About")
st.sidebar.info("""
This app uses the **VADER Sentiment Analysis** model to evaluate the sentiment of user-provided text.  
Created with ❤️ using [Streamlit](https://streamlit.io).
""")

# User input for sentiment analysis
st.subheader("Enter a sentence:")
sentence = st.text_input("Type your sentence below:")

# Analyze sentiment if a sentence is entered
if sentence:
    # Use VADER to compute sentiment scores
    scores = sia.polarity_scores(sentence)
    compound_score = scores['compound']
    
    # Determine sentiment category
    if compound_score >= 0.05:
        sentiment = "Positive 😊"
    elif compound_score <= -0.05:
        sentiment = "Negative 😔"
    else:
        sentiment = "Neutral 😐"
    
    # Display the results
    st.write("### Sentiment Analysis Result:")
    st.markdown(f"**Sentiment:** {sentiment}")
    st.markdown(f"**Compound Score:** {compound_score:.2f}")
    st.markdown(f"""
    - **Positive:** {scores['pos']:.2f}  
    - **Neutral:** {scores['neu']:.2f}  
    - **Negative:** {scores['neg']:.2f}
    """)

# Footer with decoration
st.markdown("---")
st.markdown("""
<style>
footer {visibility: hidden;}
.reportview-container .main footer {visibility: hidden;}
header {visibility: hidden;}
</style>
<div style="text-align: center; color: gray;">
    <small>Developed with ❤️ by [NURUL DINI FAQRIAH]</small>
</div>
""", unsafe_allow_html=True)
