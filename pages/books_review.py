import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Avaliações de Livros", page_icon="📚")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("📚 Selecione um Livro", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book["book price"].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]
book_author = df_book["author"].iloc[0]
book_url = df_book["url"].iloc[0]

# --- Cabeçalho ---
st.title(book_title)
st.subheader(f"Escrito por {book_author}")
st.markdown(f"**Gênero:** {book_genre}")

if pd.notna(book_url):
    st.link_button("🛒 Comprar / Acessar Livro", book_url)

st.divider()

# --- Métricas ---
col1, col2, col3 = st.columns(3)

col1.metric("💰 Preço", book_price)
col2.metric("⭐ Avaliação", book_rating)
col3.metric("📅 Ano de Publicação", book_year)

st.divider()

# --- Avaliações ---
st.header("Avaliações de Clientes 💬")

if len(df_reviews_f) == 0:
    st.info("Ainda não há avaliações de clientes para este livro.")
else:
    for row in df_reviews_f.values:
        message = st.chat_message(row[3])
        message.write(f"**{row[2]}** ({row[4]} ⭐)")
        message.write(row[5])
