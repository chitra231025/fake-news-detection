import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

<<<<<<< HEAD
st.title("📰 Fake News Detection")
st.write("Enter a news headline and click Predict.")

# Text Input
=======
# Page setup
st.set_page_config(page_title="Fake News Detection", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>📰 Fake News Detection</h1>
    <p style='text-align: center;'>Enter a news headline and click Predict.</p>
""", unsafe_allow_html=True)

# Input text
>>>>>>> b34746d7a93d5a850e7e63809e6ae10435496b84
user_input = st.text_input("News text:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
<<<<<<< HEAD
        X = vectorizer.transform([user_input])
        pred = model.predict(X)[0]   # 0 or 1

        if pred == 1:
=======
        x = vectorizer.transform([user_input])
        pred = model.predict(x)[0]

        if pred == "fake" or pred == 1:
>>>>>>> b34746d7a93d5a850e7e63809e6ae10435496b84
            st.error("Fake News")
        else:
            st.success("Real News")
