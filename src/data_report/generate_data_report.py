import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import os, sys
from src.exception import CustomException


class DashboardGenerator:
    def __init__(self, data):
        self.data = data

        # Convert 'Over_All_Rating' and 'Price' columns to numeric
        self.data['Over_All_Rating'] = pd.to_numeric(self.data['Over_All_Rating'], errors='coerce')
        self.data['Price'] = pd.to_numeric(
        self.data['Price'].apply(lambda x: x.replace("₹", "")),errors='coerce')
        self.data["Rating"] = pd.to_numeric(self.data['Rating'], errors='coerce')


# -------------------- GENERAL INFO 

    def display_general_info(self):
        product_count = self.data["Product Name"].nunique()
        
        if product_count == 1:
            return

        st.header('General Information')

        # Summary pie chart of average ratings by product
        product_ratings = self.data.groupby('Product Name', as_index=False)['Over_All_Rating'].mean().dropna()
        product_ratings = product_ratings.sort_values(by='Over_All_Rating', ascending=False)

        # Create short labels for pie
        product_ratings['Short Name'] = (product_ratings['Product Name'].str.slice(0, 25) + '...')

        fig_pie = px.pie(
            product_ratings,
            values='Over_All_Rating',
            names='Short Name',
            title='Average Ratings by Product',
            hole=0.4,                       
            hover_data=['Product Name']   
        )

        fig_pie.update_layout(
            legend_title_text='Products',
            height=450
        )


        st.plotly_chart(fig_pie)


        # Bar chart comparing average prices of different products with different colors
        avg_prices = self.data.groupby('Product Name', as_index=False)['Price'].mean().dropna()
        avg_prices['Product_ID'] = [f'Product {i+1}' for i in range(len(avg_prices))]

        fig_bar = px.bar(avg_prices, 
                         x='Price', 
                         y='Product_ID', 
                         orientation= 'h',
                         title='Average Price Comparison Between Products',
                         hover_data=['Product Name']    
        )
        
        fig_bar.update_layout(
            xaxis_title='Average Price',
            yaxis_title='Products',
            showlegend=False,
            height=500
        )
        st.plotly_chart(fig_bar)    

# -------------------- RENDER HELPERS

    def render_product_summary(self, product_data):
        st.markdown(f"💰 **Avg Price:** ₹{product_data['Price'].mean():.2f}")
        st.markdown(f"⭐ **Avg Rating:** {product_data['Over_All_Rating'].mean():.2f}")

    def render_positive_reviews(self, product_data):
        positive_reviews = (
            product_data[product_data["Rating"] >= 4.5]
            .nlargest(5, "Rating")
        )
        for _, row in positive_reviews.iterrows():
            st.markdown(f"✨ {row['Rating']} — {row['Comment']}")

    def render_negative_reviews(self, product_data):
        negative_reviews = (
            product_data[product_data["Rating"] <= 2]
            .nsmallest(5, "Rating")
        )
        for _, row in negative_reviews.iterrows():
            st.markdown(f"💢 {row['Rating']} — {row['Comment']}")

    def render_rating_counts(self, product_data):
        rating_counts = (
            product_data["Rating"]
            .value_counts()
            .sort_index(ascending=False)
        )
        for rating, count in rating_counts.items():
            st.write(f"🔹 Rating {rating} count: {count}")
    
    def render_product_description(self, product_data):
        comments = " ".join(
            product_data["Comment"].dropna().head(10)
        )
        st.text_area("", comments, height=220)


# -------------------- PRODUCT SECTIONS 

    def display_product_sections(self):
        st.header("Product Sections")

        # Works for 1 product or many
        product_names = self.data["Product Name"].unique()

        for product_name in product_names:
            st.subheader(product_name)
            product_data = self.data[self.data["Product Name"] == product_name]

            sections = [
                ("Negative Reviews", lambda d=product_data: self.render_negative_reviews(d)),
                ("Rating Counts", lambda d=product_data: self.render_rating_counts(d)),
                ("Product Summary", lambda d=product_data: self.render_product_summary(d)),
                ("Positive Reviews", lambda d=product_data: self.render_positive_reviews(d)),
                ("Product Description", lambda d=product_data: self.render_product_description(d)),
            ]

            cols_per_row = 3

            for i in range(0, len(sections), cols_per_row):
                row_sections = sections[i : i + cols_per_row]
                cols = st.columns(len(row_sections))

                for col, (title, render_fn) in zip(cols, row_sections):
                    with col:
                        st.markdown(f"### {title}")
                        render_fn()

            st.markdown("---")