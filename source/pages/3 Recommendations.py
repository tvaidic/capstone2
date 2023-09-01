from pathlib import Path
import streamlit as st
st.set_page_config(
    page_title = "Recommendations",
    page_icon = '🐱‍🏍',
)
st.title('Find a Similar Weapon')
import sys
import os
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)
from tomongo import ToMongo
c = ToMongo()
cursor = c.weapons.find()
df = pd.DataFrame(list(cursor))
df.fillna(0, inplace=True)
for col in df.keys():
    if df[col].dtype !='O':
        df[col] = df[col].astype(float)
st.title("Weapon Recomendation System")
selected_weapon = st.selectbox("Select Weapon", df["name"])
def calculate_weapon(weapon1, weapon2):
    stats1 = weapon1[['req_str', 'req_dex', 'req_int', 'req_fai', 'req_arc']].values
    stats2 = weapon2[['req_str', 'req_dex', 'req_int', 'req_fai', 'req_arc']].values
    return euclidean_distances(stats1.reshape(1, -1), stats2.reshape(1, -1))[0][0]

if not df.empty:
    selected_weapon_info = df[df['name'] == selected_weapon]
    if not selected_weapon_info.empty:
        df['similarity'] = df.apply(lambda row: calculate_weapon(selected_weapon_info, row), axis=1)
        df = df[df['name'] != selected_weapon]
        df = df.sort_values(by='similarity').head(3)
        st.subheader("Recommended Weapons")
        for index, row in df.iterrows():
            st.write("Name:", row['name'])
            st.image(row['image'])
            st.write("Category:", row['category'])
            st.write("Similarity Score:", row['similarity'])
            st.write("Required Stats:")
            st.data_editor(row[['req_str', 'req_dex', 'req_int', 'req_fai', 'req_arc']].to_dict())
            st.write("----------")
