import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

# Title and description
st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon top-selling books from 2009 to 2022.")

# --- Summary Statistics ---
st.subheader("Summary Statistics")

total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

# --- Dataset Preview ---
st.subheader("Dataset Preview")
st.write(books_df.head())

# --- Top Titles and Authors ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Book Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

# --- Genre Distribution ---
st.subheader("Genre Distribution")
fig = px.pie(
    books_df,
    names="Genre",
    title="Most Liked Genres (2009–2022)",
    color='Genre',
    color_discrete_sequence=px.colors.qualitative.D3
)
st.plotly_chart(fig)

# --- Fiction vs Non-Fiction over Years ---
st.subheader("Number of Fiction vs Non-Fiction Books Over the Years")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name="Count")
fig = px.bar(size, x="Year", y="Count", color="Genre", barmode="group", title="Books per Genre per Year")
st.plotly_chart(fig)

# --- Filter Data by Genre ---
st.subheader("Filter Data by Genre")
genre_filter = st.selectbox("Select Genre", books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]
st.write(filtered_df.head())
