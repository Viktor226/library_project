import streamlit as st
st.title("Biblioteka")
if "books" not in st.session_state:
  st.session_state.books = []

st.header("dobawi kniga")
title = st.text_input("zaglawie")
author= st.text_input("awtor")
price = st.text_input("cena", min_value=0.0)
if st.button("dobawi knigata"):

 book = {
  "title": title,
  "author": author,
  "price" : price,
}

st.session_stete.books.append(book)
st.success("knigata e dobawena")
 

if st.button("pokaji wsichki knigi"):
  st.write("няма добавени книги")
else:
  for book in st.session_stete.books:
    st.write("zaglawie:", book["title"])
    st.write("awtor :", book["author"])
    st.write("cena:", book["price"])
    st.write("---------------------------")
st.header("tursene po awtor")
search_author = st.text_input("wuwedi awtor, koito iskash da namerish")
if st.button("tursi po avtor"):
 found = false
 for book in st.session_state.books:
  if book["author"] == search_author:
   st.write(book)
   found = True


st.header = ("tursi po zaglawie")
search_title = st.text_input("wuwedi zaglawie")

if st.button("tursi po zaglawie")

found = False
for book in st.session_state.books:
  if book ["title"] == search_title:
    st.write(book, "e namerena")
 found = True

if found == false:
  st.write("kniga ne e namerena")

if st.button("pokaji nai- evtina kniga"):

if len(session_state.books) == 0:
  st.error("nqma knigi")

else :
  cheapest = session_state.books[0]

for book in session_state.books:
  if book["price"] < cheapest["price"]:
    chapest = book["price"]
  st.write(cheapest)



