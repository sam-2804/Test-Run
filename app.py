import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load the hidden .env file
load_dotenv()

# Initialize the Google GenAI client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("🔥 PitchRoast AI")
st.write("Paste your startup pitch below. Our AI VC will tear it apart.")

# Create a large text box
user_pitch = st.text_area("Your Pitch:", height=150)

# When the user clicks the button...
if st.button("Roast My Pitch"):
    if user_pitch.strip() == "":
        st.error("Please enter a pitch first!")
    else:
        # Show a loading spinner while the API works
        with st.spinner("The VC is reading..."):
            
            # The Magic Prompt
            prompt = f"""
            Act as a ruthless, highly critical Silicon Valley Venture Capitalist. 
            Read the following startup pitch and provide:
            1. A 'Roast Score' out of 10.
            2. A brutal, honest paragraph explaining why it will fail.
            3. A constructive 1-sentence rewrite to make it actually fundable.
            
            Here is the pitch: {user_pitch}
            """
            
            # Call the AI
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            
            # Display the output beautifully
            st.markdown(response.text)