import streamlit as st

# Judul aplikasi
st.title("🎧 Audio Playback Interface")

# Upload file audio
uploaded_file = st.file_uploader("Upload file audio", type=["mp3", "wav"])

# Jika ada file yang diupload
if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')
    st.success("File berhasil dimuat, silakan tekan play untuk mendengarkan.")
else:
    st.info("Silakan upload file audio terlebih dahulu.")
