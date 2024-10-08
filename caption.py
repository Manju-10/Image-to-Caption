import requests
import streamlit as st
import base64

def get_img_as_base64(url):
    response = requests.get(url)
    return base64.b64encode(response.content).decode()

img_url = "https://wallpapercave.com/wp/ibG1tbs.jpg"
img = get_img_as_base64(img_url)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}}
[data-testid="stHeader"]{{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set custom title with HTML/CSS for blue glow effect on both text and icon
st.markdown(
    """
    <h1 style="text-align: center; color: #00BFFF; font-size: 50px;
    text-shadow: 0 0 10px #00BFFF;
    filter: brightness(1.5);">
    <img src="https://icon-library.com/images/ai-icon/ai-icon-7.jpg" alt="icon" 
    style="width:50px;height:50px;vertical-align:middle;margin-right:10px;
    filter: brightness(2);">
    Image to Caption AI
    </h1>
    """,
    unsafe_allow_html=True
)

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(file):
    response = requests.post(API_URL, headers=headers, data=file)
    return response.json()

uploaded_file = st.file_uploader("Upload an image", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate"):
        output = query(uploaded_file.getvalue())
        caption = output[0]["generated_text"]  # Extract the caption
        st.write("**Generated Caption:**", caption)  # Display the caption text only
else:
    st.write("Please upload an image file.")
