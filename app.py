import streamlit as st
import matplotlib.pyplot as plt

from utils.audio_utils import load_audio
from utils.inference import run_inference

st.title("Bengali Dialect Identification")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file:
    audio = load_audio(uploaded_file)
    st.audio(uploaded_file)

    with st.spinner("Predicting dialect..."):
        results = run_inference(audio)

    st.subheader("Top Predictions")
    for label, score in results[:3]:
        st.write(f"{label}: {score:.2f}")

    labels = [x[0] for x in results]
    scores = [x[1] for x in results]

    fig, ax = plt.subplots()
    ax.barh(labels, scores)
    ax.invert_yaxis()
    st.pyplot(fig)
