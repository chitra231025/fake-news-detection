import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("📰 Fake News Detection")
st.write("Enter a news headline and click Predict.")

# Text Input
user_input = st.text_input("News text:")

# Predict Button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        X = vectorizer.transform([user_input])
        pred = model.predict(X)[0]   # 0 or 1

        if pred == 1:
            st.error("Fake News")
        else:
            st.success("Real News")
