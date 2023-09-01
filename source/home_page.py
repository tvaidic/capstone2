import streamlit as st
st.set_page_config(
    page_title = "Elden Arms",
    page_icon = '🐱‍🏍',
)

st.title('Elden Arms')
st.image(r'https://i.redd.it/3e2afpjsi4f61.png')
st.text('Your one stop shop for all your weapon stats recomendations')

st.header('Heres a list of the pages and functionality')
st.subheader('Weapon Search')
st.text('Search a weapon and return all information including stats, images, and descriptions')

st.subheader('Stats')
st.text('See trends of your choice')


st.subheader('Recomendations')
st.text('Get recomendations based on an input  of a stat or weapon')