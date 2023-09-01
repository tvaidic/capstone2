from pathlib import Path
import streamlit as st
st.set_page_config(
    page_title = "Weapon Info",
    page_icon = "🐱‍🏍"
)
import sys
import os
from PIL import Image
from io import BytesIO
import pandas as pd
filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from tomongo import ToMongo
c = ToMongo()
cursor = c.weapons.find()
df = pd.DataFrame(list(cursor))
df.fillna('None', inplace=True)
# weapons_list = df.name.tolist()
st.title('Weapons Info')
selected_weapon = st.selectbox('Search a weapon', df['name'])
column1, column2 = st.columns(2)
weapon_info = df[df['name'] == selected_weapon].iloc[0]
with column1:
    st.image(weapon_info['image'], caption=weapon_info['description'],width=300)

st.subheader('Weapon Information')
col1, col2, col3, col4 = st.columns(4)
#st.write("About the weapon:", weapon_info['description'])
with column2:
    
    st.write("Category:", weapon_info['category'])
    st.write("Weight:", weapon_info['weight'])
with col1:
    st.subheader("Required Attributes")
    st.write("Strength:", weapon_info['req_str'])
    st.write("Dexterity:", weapon_info['req_dex'])
    st.write("Intelligence:", weapon_info['req_int'])
    st.write("Faith:", weapon_info['req_fai'])
    st.write("Arcane:", weapon_info['req_arc'])
with col2:
    st.subheader("Scaling Attributes")
    st.write("Strength:", weapon_info['scl_str'])
    st.write("Dexterity:", weapon_info['scl_dex'])
    st.write("Intelligence:", weapon_info['scl_int'])
    st.write("Faith:", weapon_info['scl_fai'])
    st.write("Arcane:", weapon_info['scl_arc'])
with col3:
    st.subheader("Attack Attributes")
    st.write("Physical Attack:", weapon_info['phys_attack'])
    st.write("Magic Attack:", weapon_info['magic_attack'])
    st.write("Fire Attack:", weapon_info['fire_attack'])
    st.write("Light Attack:", weapon_info['light_attack'])
    st.write("Holy Attack:", weapon_info['holy_attack'])
    st.write("Critical Attack:", weapon_info['crit_attack'])
with col4:
    st.subheader("Defense Attributes")
    st.write("Physical Defense:", weapon_info['phys_defence'])
    st.write("Magic Defense:", weapon_info['magic_defence'])
    st.write("Fire Defense:", weapon_info['fire_defence'])
    st.write("Light Defense:", weapon_info['light_defence'])
    st.write("Holy Defense:", weapon_info['holy_defence'])
    st.write("Boost Defense:", weapon_info['boost_defence'])
