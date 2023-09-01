from pathlib import Path
import streamlit as st
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
weapons_list = df.name.tolist()
select = st.selectbox('Search a weapon', options = weapons_list)
if select:
    st.subheader(select)
    st.image(df['image'])