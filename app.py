import streamlit as st
st.title("Библиотека")
if "books" not in st.session_state:
  st.session_state.books = []

st.header("Добави книга")
title = st.text_input("zaglawie")
author= st.text_input("awtor")
price = st.text_input("cena", min_value=0.0)
if st.button("Добави книга"):

 book = {
  "title": title,
  "author": author,
  "price" : price,
}

st.session_stete.books.append(book)
st.success("Книгата е добавена")
 

if st.button("Покажи всички книги"):
  st.write("няма добавени книги")
else:
  for book in st.session_stete.books:
    st.write("Заглавие:", book["title"])
    st.write("Автор :", book["author"])
    st.write("Цена:", book["price"])
    st.write("---------------------------")
st.header("Търсене по автор")
search_author = st.text_input("Въведи автор, които искаш да намериш")
if st.button("Търси по автор"):
 found = false
 for book in st.session_state.books:
  if book["author"] == search_author:
   st.write(book)
   found = True


st.header = ("Търси по заглавие")
search_title = st.text_input("Въведи заглавие")

if st.button("Търси по заглавие"):

 found = False
 for book in st.session_state.books:
   if book ["title"] == search_title:
     st.write(book, "е намерена")
     found = True

if found == false:
  st.write("книга не е намерена")

if st.button("Покайи наи-евтина книга"):
 if len(session_state.books) == 0:
  st.error("няма книги")

else :
  cheapest = session_state.books[0]

for book in session_state.books:
  if book["price"] < cheapest["price"]:
    chapest = book["price"]
  st.write(cheapest)



