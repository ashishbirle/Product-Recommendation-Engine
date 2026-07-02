import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("dataset/indian_ecommerce_dataset.csv")

# Feature Engineering
df['Features'] = df['Category'] + ',' + df['Brand'] + ',' + df['Description']

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform the features to create a TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(df['Features'])

# Compute cosine similarity between products
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get product recommendations based on a given product index
def recommend_products(product_name, min_price=0, max_price=150000):
    # Get the index of the product that matches the name
    idx = df[df['Product_Name'] == product_name].index[0]
    
    # Get the similarity scores for the product
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the products based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 5 most similar products
    # sim_scores = sim_scores[1:6]
    
    # sim_scores = sim_scores[1:6]
    # if max_price:
    product_indices = [i for i,s in sim_scores if min_price <= df['Price'][i] <= max_price][1:6]
    # else:    
    #     product_indices = [x[0] for x in sim_scores][1:6]
    # Return the recommended products
    return df[['Product_Name','Category','Brand','Price','Rating']].iloc[product_indices]

product_recommendations = recommend_products

# try:
#     product_name = input("Enter the product name:")
    
#     if not product_name:
#         raise ValueError("Product name cannot be empty.")
#     elif product_name not in df['Product_Name'].values:
#         raise ValueError("Product not found in the dataset.") 
#     print(recommend_products(product_name))
# except ValueError as e:
#     print(f"Error: {e}")
