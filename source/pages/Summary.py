import streamlit as st
st.set_page_config(
    page_title = 'Summary',
    page_icon = "📜")
st.header('Elden Arms Summary')
st.markdown("""This application is built using the Elden Ring API (https://eldenring.fanapis.com/). The application uses a base.py page that loads in the Elden Ring Api. The base page then has a class called 'base' the base class combines the multiple pages of weapons from the api and then cleans the data. Initially the data has a lot of nested lists and dictionaries so the clean data function itterates through the dictionaries and appends them to new lists. After appending them to new lists they are added as columns the dataframe and the original columns are dropped. After doing so it saves the data to a csv file to be used later.
""")
st.markdown(''' The app then uses a tomongo.py page that connects to a NoSQL database and inserts the data one instance at a time.
''')
st.markdown(''' The rest of the pages are now features of the app itself. Outside of the landing page, The first page that is the Weapons Serch page which queries the data from MongoDB and returns weapon category, weapon weight, required attributes for the weapon, how the weapon stats scale, the different types of damage stats the weapon does and the defensive stats of the weapon.  ''')
st.markdown('''The Stats page queries the cateory of weapon and a statistic by user choice. Then a bar chart is returned displaying all the weapons in the category and the respective stats for each one allowing the user to find the best possible stats for a specific type of weapon''')
st.markdown('''Finally the recommendations lets the user query a weapon and uses the Euclidian distances model from sklearn to measure the distance between two points on a euclidian plane. The smaller the value the more similar the weapon. The page is set to return the three closest weapons to what the user inputs. This allows the user to discover weapons similar to one they may be using''')
st.markdown('''Future additions to this could include linking the sheild, armour, ashes of war, and sorcery data also in the same api allowing the user to search stats for those as well. Additional recommendations could also be included''')
st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')