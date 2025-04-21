import streamlit as st
import os
from src.textSummarizer.pipeline.prediction import PredictionPipeline

# Page config
st.set_page_config(page_title="Text Summarizer", layout="centered")

# Title
st.title("📝 Text Summarization App")
st.markdown("This app uses a fine-tuned transformer model to summarize text intelligently.")

# Training section
with st.expander("🧠 Train the Model"):
    st.markdown("In order to train the model, click below.")
    if st.button("Train Model"):
        with st.spinner("Training in progress... this might take a while ⏳"):
            try:
                os.system("python main.py")  # make sure main.py triggers training
                st.success("✅ Model trained successfully!")
            except Exception as e:
                st.error(f"❌ Training failed: {e}")

# Text area for input
st.subheader("🔍 Generate Summary")
input_text = st.text_area("Enter the text you want to summarize", height=300)

# Summarize button
if st.button("Summarize", type="primary"):
    if input_text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Summarizing..."):
            try:
                obj = PredictionPipeline()
                summary = obj.predict(input_text)
                st.subheader("📄 Summary:")
                st.success(summary)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
