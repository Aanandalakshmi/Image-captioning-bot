import streamlit as st
from PIL import Image
from blip_model import generate_caption

st.set_page_config(page_title="Image Captioning Bot", layout="centered")

st.title("Image captioning with Blip")
st.caption("Upload an image and get a natural-language description")

uploaded_file=st.file_uploader("Choose an image", type=["jpg","jpeg","png"])

if uploaded_file:
    image=Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    with st.spinner("Generating caption..."):
        caption=generate_caption(image)
    st.success("Caption Generated!")
    st.markdown(f"Caption: _{caption}_")