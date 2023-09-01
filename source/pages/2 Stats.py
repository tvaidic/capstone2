from pathlib import Path
import streamlit as st
st.set_page_config(
    page_title = "Stats",
    page_icon = '🐱‍🏍',
)
st.title("Weapons Stats")
import sys
import os
import pandas as pd
filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)
from tomongo import ToMongo
c = ToMongo()
cursor = c.weapons.find()
df = pd.DataFrame(list(cursor))
df.fillna(0, inplace=True)
#df['phys_attack'] = df['phys_attack'].astype(int)
for col in df.keys():
    if df[col].dtype !='O':
        df[col] = df[col].astype(int)
w_list = list(set(df['category'].tolist()))

x = st.selectbox(label = 'Pick a category',options = sorted(w_list))
y = st.selectbox(label = 'Pick a Stat', options = ['weight','req_str','req_dex','req_int','req_fai','req_arc','phys_attack','magic_attack','fire_attack','light_attack','holy_attack','crit_attack','phys_defence','magic_defence','fire_defence','light_defence','holy_defence','boost_defence'])
xdf = df[df['category']== x]
edf = pd.DataFrame({f'{x}': xdf['name'], f"{y.title().replace('_',' ')}": xdf[y]})

st.bar_chart(data = edf, x=edf.keys()[0], y=edf.keys()[1],)



