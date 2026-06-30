import pandas as pd
from e_commerce_recommendation import product_recommendations
import streamlit as st

image_url = "https://raw.githubusercontent.com/ashishbirle/product-recommendation-engine/refs/heads/main/background_image/img_recommendation.png"


def set_github_background(url):
    page_bg_img = f'''
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: local;
    }}
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)

set_github_background(image_url)
# The above code is to set up a background image for to the streamlit application.

st.title("Welcome to Product Recommendation Engine")
df = pd.read_csv("dataset/indian_ecommerce_dataset.csv")

validity = 0
try:
    product_name = st.text_input("Enter the product name:")
    if st.button("Check validity"):
        if not product_name:
            raise ValueError("Product name cannot be empty.")
        elif product_name not in df['Product_Name'].values:
            raise ValueError("Product not found in the dataset.")
        else:
            st.write("Valid Product")

except ValueError as e:
    st.write(f"Error: {e}")


if st.button("Recommend"):
    recommendation = product_recommendations(product_name)
    st.write(recommendation)
