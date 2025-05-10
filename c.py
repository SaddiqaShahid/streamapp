import streamlit as st
import requests

# --- Config ---
API_KEY = "sk_d4c221b78e782393191ba3a80e6bba310b83d540e8779153"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel

# --- Page Config ---
st.set_page_config(page_title=" SS Text to Speech", page_icon="🗣️", layout="centered")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        .main-title {
            font-size: 3rem;
            font-weight: 700;
            color: #003566;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            font-size: 1.1rem;
            color: #555;
            text-align: center;
            margin-bottom: 2rem;
        }
        .footer {
            text-align: center;
            color: #999;
            font-size: 0.85rem;
            margin-top: 4rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">🗣️ SS Text to Speech</div>', unsafe_allow_html=True)


# --- Input Text Area ---
text_input = st.text_area("✍️ Enter the text below", height=200, placeholder="Write your message here...")

# --- TTS Function ---
def generate_audio(text, filename="output.mp3"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        return filename
    else:
        st.error("❌ Error generating audio")
        st.code(response.text)
        return None

# --- Generate Button ---
if st.button("🎧 Convert to Voice"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        with st.spinner("🔊 Generating voice..."):
            output = generate_audio(text_input)
            if output:
                st.success("✅ Voice generated successfully!")
                audio_bytes = open(output, "rb").read()
                st.audio(audio_bytes, format="audio/mp3")

